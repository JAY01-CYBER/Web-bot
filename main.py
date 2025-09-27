import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from fastapi import FastAPI
import uvicorn

# 🔑 Load credentials from env vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

# ✅ Init Telethon client
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# ✅ Init FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "✅ Userbot + Web server is running on Render!"}

# 🔹 Healthcheck endpoint
@app.get("/health")
async def health():
    return {"ok": True}

# Example command
@client.on(events.NewMessage(pattern="!ping"))
async def ping(event):
    await event.reply("pong ✅")

# 🔹 Start bot + API
async def start_bot():
    print("🚀 Starting Telethon client...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Start Telethon in background
    loop.create_task(start_bot())

    # Start FastAPI (Render will detect this port)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
