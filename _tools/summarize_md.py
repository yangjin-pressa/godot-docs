import os
import requests
import json

# 设置输入和输出目录
input_dir = 'E:\Git\godot-docs\md'
output_dir = 'E:\Git\godot-docs\md2'
os.makedirs(output_dir, exist_ok=True)

# 遍历目录中的所有 .md 文件
for filename in os.listdir(input_dir):
    if filename.endswith('.md'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # 读取原始内容
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 构建请求数据
        prompt = f"用英文精简以下内容（不要包含任何 <think> 或内部思考内容）：\n\n{content}"
        data = {
            "model": "qwen3:4b",
            "prompt": prompt,
            "stream": True
        }

        # 发送请求到 Ollama
        try:
            response = requests.post('http://localhost:11434/api/generate', json=data, stream=True)
            response.raise_for_status()

            summarized_content = ''
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        json_data = json.loads(line)
                        part = json_data.get('response', '')
                        # 跳过 <think> 段落
                        if "<think>" in part or "</think>" in part:
                            continue
                        summarized_content += part
                    except json.JSONDecodeError as e:
                        print(f"JSON 解码错误：{e}")
                        continue

            # 保存精简后的内容
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summarized_content)
            print(f"已处理并保存：{output_path}")

        except requests.exceptions.RequestException as e:
            print(f"请求错误：{e}")
