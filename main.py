from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os, asyncio
from fastapi import FastAPI
import uvicorn

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "✅ Bot is running with StringSession"}

@client.on(events.NewMessage(pattern="!ping"))
async def handler(event):
    await event.reply("pong ✅")

async def main():
    await client.start()
    server = uvicorn.Server(uvicorn.Config(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000))))
    await asyncio.gather(client.run_until_disconnected(), server.serve())

if __name__ == "__main__":
    asyncio.run(main())
