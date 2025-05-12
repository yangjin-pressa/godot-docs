from __future__ import annotations

import os
import asyncio
import re

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

# ✍️ 创建 Agent（模型行为）
agent = Agent(
    name="MarkdownSummarizer",
    instructions=(
        "To ensure that instructions are concise and remain true to the original content without adding extra information, follow these guidelines"
        "Tables: Extract key data points and summarize their purpose and content. Ensure all essential information is retained for understanding functionality or configuration."
        "Images: Describe the image content briefly and highlight its relevance to the topic. Focus on any visual aids that clarify complex concepts or show step-by-step procedures."
        "References: Summarize key points from cited references and explain their significance to the document. Include any crucial external links or additional readings that offer deeper insights."
        "Remove repetitive and non-essential content while maintaining clarity and usability of the information."
        "Avoid using headings, markdown syntax, and extra formatting. Focus on presenting the essence of the information straightforwardly and understandably."
    ),
)
def clean_output(output: str) -> str:
    # Remove <think>...</think> block including multiline
    return re.sub(r"<think>.*?</think>\s*", "", output, flags=re.DOTALL)

# 📄 精简单个文件
async def summarize_file(file_path: str, output_path: str):
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

    print(f"✅ 已处理: {os.path.basename(file_path)}")

# 🔁 批量处理目录下所有 .md 文件
async def main():
    tasks = []
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename)
            tasks.append(summarize_file(input_path, output_path))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
