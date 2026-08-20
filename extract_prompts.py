import json
import os

transcript_path = r"C:\Users\kirta\.gemini\antigravity-ide\brain\75fcc86b-90ae-4b3c-8cec-7d904bc307f9\.system_generated\logs\transcript.jsonl"
prompts_file = "D:\Projects\airbnb-clone\ai_prompts.txt"

with open(transcript_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

prompts = []
for line in lines:
    try:
        data = json.loads(line)
        if data.get("type") == "USER_INPUT":
            prompts.append(data.get("content", ""))
    except:
        pass

with open(prompts_file, "w", encoding="utf-8") as f:
    f.write("Sequence of prompts used for AI-assisted development:\n\n")
    for i, p in enumerate(prompts):
        f.write(f"Prompt {i+1}:\n{p}\n\n")

print(f"Extracted {len(prompts)} prompts")
