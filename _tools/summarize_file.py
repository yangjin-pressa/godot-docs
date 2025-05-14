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

# Add force rewrite control variable
FORCE_REWRITE = False  # Set to True to force reprocessing of existing files

def log(message: str, level: str = "INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

INPUT_DIR = "E:\Git\godot-docs\classes2md"
OUTPUT_DIR = "E:\Git\godot-docs\md2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

load_dotenv()
BASE_URL = os.getenv("EXAMPLE_BASE_URL")
API_KEY = os.getenv("EXAMPLE_API_KEY")
MODEL_NAME = os.getenv("EXAMPLE_MODEL_NAME")
set_tracing_disabled(True)

def check_ollama_running(retries=3, delay=2) -> bool:
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

def start_ollama():
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

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

class CustomModelProvider(ModelProvider):
    def get_model(self, model_name: str | None) -> Model:
        return OpenAIChatCompletionsModel(
            model=model_name or MODEL_NAME,
            openai_client=client,
        )

CUSTOM_MODEL_PROVIDER = CustomModelProvider()

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
    file_name = os.path.basename(file_path)
    
    # Check if output file already exists and skip if not forcing rewrite
    if os.path.exists(output_path) and not FORCE_REWRITE:
        log(f"Skipped (already exists): {file_name}")
        pbar.update(1)
        pbar.set_description(f"Skipped {file_name[:15]}...")
        return
    
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
    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.endswith(".md")
    ]
    
    if not files:
        log("No Markdown files found", "WARNING")
        return

    # Log whether force rewrite is enabled
    if FORCE_REWRITE:
        log("Force rewrite mode enabled - will reprocess all files")
    else:
        log("Skip existing files mode enabled - will skip already processed files")
        
    log(f"Starting batch processing ({len(files)} files)")
    files_processed = 0
    batch_size = 5
    with tqdm_asyncio(
        total=len(files),
        desc="📊 Progress",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        dynamic_ncols=True,
        mininterval=0.5
    ) as pbar:
        sem = asyncio.Semaphore(10)
        while files_processed < len(files):
            batch_files = files[files_processed:files_processed + batch_size]
            if not check_ollama_running():
                start_ollama()
            tasks = [
                wrapped_task(f, sem, pbar)
                for f in batch_files
            ]
            await asyncio.gather(*tasks)
            
            files_processed += batch_size
            if files_processed > len(files):
                files_processed = len(files)
    log("All files processed")

async def wrapped_task(filename, sem, pbar):
    async with sem:
        await summarize_file(
            file_path=os.path.join(INPUT_DIR, filename),
            output_path=os.path.join(OUTPUT_DIR, filename),
            pbar=pbar
        )

def shutdown_handler(signum, frame):
    log("Shutting down gracefully...", "WARNING")
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