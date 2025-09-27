import os
import asyncio
from telethon import TelegramClient, events
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from typing import List

# 🔹 Load credentials from environment
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
SESSION = os.getenv("SESSION", "your_session")

# 🔹 Init Telegram client
client = TelegramClient(SESSION, API_ID, API_HASH)

# 🔹 Init FastAPI app
app = FastAPI(title="Telegram Userbot API", version="1.0")

@app.get("/")
async def root():
    return {"status": "✅ Userbot + Web server running!"}

@app.get("/send/{chat_id}/{msg}")
async def send_msg(chat_id: int, msg: str):
    await client.send_message(chat_id, msg)
    return {"sent": True, "chat_id": chat_id, "message": msg}

@app.post("/broadcast/")
async def broadcast(chats: List[int], msg: str):
    results = []
    for chat in chats:
        try:
            await client.send_message(chat, msg)
            results.append({"chat_id": chat, "status": "✅ sent"})
        except Exception as e:
            results.append({"chat_id": chat, "status": f"❌ failed: {e}"})
    return {"broadcast_results": results}

@app.get("/dashboard")
async def dashboard():
    return FileResponse("frontend.html")

@client.on(events.NewMessage(pattern="!ping"))
async def handler(event):
    await event.reply("pong ✅")

async def main():
    await client.start()
    server = uvicorn.Server(uvicorn.Config(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000))))
    await asyncio.gather(client.run_until_disconnected(), server.serve())

if __name__ == "__main__":
    asyncio.run(main())
