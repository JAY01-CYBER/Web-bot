import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from fastapi import FastAPI
import uvicorn

# 🔑 Load credentials from env vars
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")

# ✅ Init Telethon client
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# ✅ Init FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "✅ Userbot + Web server is running on Render!"}

@app.get("/health")
async def health():
    return {"ok": True}

# Example command
@client.on(events.NewMessage(pattern="(?i)!ping"))  # (?i) => case-insensitive (!ping, !Ping, !PING)
async def ping(event):
    await event.reply("pong ✅")

# 🔹 Start bot + API with login info
async def start_bot():
    try:
        print("🚀 Starting Telethon client...")
        await client.start()
        me = await client.get_me()
        print(f"✅ Logged in as: {me.first_name} (id: {me.id}) [username: @{me.username}]")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"❌ Telethon error: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
