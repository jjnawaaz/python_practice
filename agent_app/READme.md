📬 Job Email AI Agent → Discord Alerts

This project is an agentic AI system that:

• Reads unread Gmail job emails
• Uses an LLM to classify job opportunities
• Extracts role, company & urgency
• Sends job alerts directly to Discord

🚀 Features

Gmail OAuth integration (secure access)

AI-powered email triage (LLM brain)

Discord webhook notifications

Modular agent architecture

📁 Project Structure
agent_app/
├── agent_runner.py
├── gmail_tool.py
├── llm_brain.py
├── agent_brain.py
├── message_formatter.py
├── discord_tool.py
├── requirements.txt
├── .env.example
└── .gitignore

🔧 Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/yourusername/job-email-ai-agent.git
cd agent_app

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate # Mac / Linux
venv\Scripts\activate # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Google Gmail API Setup

Go to Google Cloud Console

Create a new project

Enable Gmail API

Create OAuth Client → Desktop App

Download credentials.json

Place it inside project root

Do NOT commit this file.

5️⃣ Create .env file

Create a file called .env:

GROK_API_KEY=your_groq_api_key_here
DISCORD_WEBHOOK_URL=your_discord_webhook_here

Only used WEBHOOK_URL for now:
Ignore these
DISCORD_CHANNEL_ID=14591Your ID
DISCORD_BOT_TOKEN=Your_bot_token

6️⃣ First-time Gmail Login

Run once:

python agent_runner.py

Browser will open → Login to Gmail → Allow access.
token.json will be auto-generated.

▶️ Run the Agent
python agent_runner.py

If job email detected → Discord alert sent 🎯

❌ Files NOT to commit

Already in .gitignore:

.env
credentials.json
token.json
venv/
**pycache**/

🧠 Architecture
Gmail Tool → LLM Brain → Agent Brain → Message Formatter → Discord Tool

This is the AI Agent workflow.
