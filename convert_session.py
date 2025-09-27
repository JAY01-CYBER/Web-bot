from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = int(input("Enter your API_ID: "))
API_HASH = input("Enter your API_HASH: ")
OLD_SESSION = input("Enter your old .session filename (without .session extension): ")

with TelegramClient(OLD_SESSION, API_ID, API_HASH) as client:
    string_session = client.session.save()
    print("\n✅ Your StringSession (copy and save this safely):\n")
    print(string_session)
