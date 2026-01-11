import os
import asyncio
import aiohttp
import certifi
import ssl
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def ssl_context():
    return ssl.create_default_context(cafile=certifi.where())

async def send_discord_message(message: str):
    ctx = ssl_context()
    connector = aiohttp.TCPConnector(ssl=ctx)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.post(WEBHOOK_URL, json={"content": message}) as resp:
            if resp.status == 204:
                print("✅ Discord notified")
            else:
                print("❌ Discord error", resp.status)

def notify_discord_sync(message: str):
    asyncio.run(send_discord_message(message))
