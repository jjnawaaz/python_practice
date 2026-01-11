import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import re

load_dotenv()

GROK_API_KEY = os.getenv('GROK_API_KEY')

client = OpenAI(
    api_key=GROK_API_KEY,
    base_url='https://api.groq.com/openai/v1'
)


SYSTEM_PROMPT="""
You are an intelligent email triage agent.

Given an email snippet, decide:

1. Is this a JOB OPPORTUNITY email?
2. If yes extract:
   - company (if found)
   - role (if found)
   - urgency (low / medium / high)
   - action = notify_discord
3. If not a job → action = ignore

Respond in strict JSON only.
"""

def analyze_email(snippet: str):
    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        input=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":snippet}
        ]
    )
    raw = response.output_text.strip()
    print("\nLLM RAW OUTPUT:\n", raw)

    # Remove ```json and ``` wrappers
    cleaned = re.sub(r"```json|```", "", raw).strip()

    try:
        parsed = json.loads(cleaned)
        return parsed
    except Exception as e:
        print("JSON PARSE FAILED:", e)
        return {
            "action": "ignore",
            "error": "invalid_llm_output"
        }