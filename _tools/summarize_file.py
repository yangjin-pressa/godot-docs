from __future__ import annotations
import os
import asyncio
import re
import time
import sys
import signal
import subprocess
import requests
from datetime import datetime
from tqdm.asyncio import tqdm_asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent,
    Model,
    ModelProvider,
    OpenAIChatCompletionsModel,
    RunConfig,
    Runner,
    set_tracing_disabled,
)

# 🛠️ 配置日志格式
def log(message: str, level: str = "INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

# 🛠️ 设置输入输出目录
INPUT_DIR = "E:\Git\godot-docs\md"
OUTPUT_DIR = "E:\Git\godot-docs\md2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

load_dotenv()

# 📦 环境变量方式配置模型信息
BASE_URL = os.getenv("EXAMPLE_BASE_URL")
API_KEY = os.getenv("EXAMPLE_API_KEY")
MODEL_NAME = os.getenv("EXAMPLE_MODEL_NAME")

# ❌ 禁用 tracing
set_tracing_disabled(True)

# 🔍 检查Ollama服务状态
def check_ollama_running(retries=3, delay=2) -> bool:
    """检查Ollama服务是否已启动"""
    for _ in range(retries):
        try:
            response = requests.get(
                url="http://localhost:11434/api/tags",
                timeout=5
            )
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(delay)
    return False

# 🚀 启动Ollama服务
def start_ollama():
    """尝试启动Ollama服务"""
    try:
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("Starting Ollama service...")
        
        if not check_ollama_running(retries=10, delay=3):
            raise RuntimeError("Ollama service startup timeout")
        print("Ollama service ready")
        
    except Exception as e:
        print(f"❌ Failed to start Ollama: {str(e)}")
        sys.exit(1)

# 🛑 卸载Ollama模型
def unload_ollama_model():
    """卸载当前使用的Ollama模型"""
    try:
        if MODEL_NAME:
            response = requests.delete(
                url=f"http://localhost:11434/api/delete",
                json={"name": MODEL_NAME},
                timeout=10
            )
            if response.status_code == 200:
                log(f"Successfully unloaded model: {MODEL_NAME}")
            else:
                log(f"Failed to unload model: {response.text}", "WARNING")
    except Exception as e:
        log(f"Model unloading error: {str(e)}", "ERROR")


# 🔌 初始化 Ollama OpenAI client
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

# 🧠 自定义 ModelProvider
class CustomModelProvider(ModelProvider):
    def get_model(self, model_name: str | None) -> Model:
        return OpenAIChatCompletionsModel(
            model=model_name or MODEL_NAME,
            openai_client=client,
        )

CUSTOM_MODEL_PROVIDER = CustomModelProvider()

# ✍️ 创建 Agent (英文版指令)
agent = Agent(
    name="MarkdownSummarizer",
    instructions=(
        "You are a specialist in extracting and organizing information from Markdown documents. "
        "Your task is to distill essential information and present it concisely.\n\n"
        "1. **Header Processing**: Identify and preserve all headers with their hierarchy. "
        "Under each header, retain only core information.\n"
        "2. **Format Simplification**: Remove unnecessary markdown formatting while preserving "
        "code blocks and method definitions. Present key points using simple bullet lists.\n"
        "3. **Table Handling**: Convert tables into readable text format, extracting key data "
        "and attributes without retaining table borders.\n"
        "4. **Reference Management**: Identify and preserve all citations. Remove redundant "
        "markers and convert to plain text links when appropriate.\n"
        "5. **Language Preservation**: Maintain the original document language throughout "
        "the processed content. Do NOT translate any text."
    ),
)

def clean_output(output: str) -> str:
    return re.sub(r"<think>.*?</think>\s*", "", output, flags=re.DOTALL)

async def summarize_file(file_path: str, output_path: str, pbar: tqdm_asyncio):
    """文件处理任务"""
    file_name = os.path.basename(file_path)
    try:
        log(f"Processing: {file_name}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        result = await Runner.run(
            agent,
            input=content,
            run_config=RunConfig(model_provider=CUSTOM_MODEL_PROVIDER),
        )
        
        cleaned = clean_output(result.final_output)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
            
        log(f"Completed: {file_name}")
        
    except Exception as e:
        log(f"Failed: {file_name} - {str(e)}", "ERROR")
        raise
    finally:
        pbar.update(1)
        pbar.set_description(f"Processed {file_name[:15]}...")

async def main():
    """主处理流程"""
    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.endswith(".md")
    ]
    
    if not files:
        log("No Markdown files found", "WARNING")
        return

    log(f"Starting batch processing ({len(files)} files)")
    
    with tqdm_asyncio(
        total=len(files),
        desc="📊 Progress",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        dynamic_ncols=True,
        mininterval=0.5
    ) as pbar:
        sem = asyncio.Semaphore(10)
        
        async def wrapped_task(filename):
            async with sem:
                await summarize_file(
                    file_path=os.path.join(INPUT_DIR, filename),
                    output_path=os.path.join(OUTPUT_DIR, filename),
                    pbar=pbar
                )
        
        tasks = [wrapped_task(f) for f in files]
        await asyncio.gather(*tasks)
    
    log("All files processed")

def shutdown_handler(signum, frame):
    log("Shutting down gracefully...", "WARNING")
    unload_ollama_model()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    try:
        if not check_ollama_running():
            start_ollama()
        asyncio.run(main())
    except KeyboardInterrupt:
        log("Operation interrupted by user", "WARNING")
    except Exception as e:
        log(f"Abnormal termination: {str(e)}", "ERROR")
    finally:
        unload_ollama_model()