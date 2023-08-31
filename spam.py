# @saddys0 my telegram, feel free to dm me

from telethon import TelegramClient, events
import asyncio

# Replace the values below with your own API ID, API hash, and session name
api_id = 23254927
api_hash = '9255c6bec27988bd08f80a54cc7d004f'
session_name = 'your_session_name'

client = TelegramClient(session_name, api_id, api_hash)

# Replace the values below with the usernames of the groups you want to target
group_usernames = ['@biscottoneroma']

# Replace the value below with the message you want to send
message = '''💰EXPRESS FARM💰
📍MEET UP ROMA CENTRO📍
🏎️DELIVERY +10€🏎️

🍫MOUSSE🍫
-10g €35
-15g €50
-20g €60
-25g €70
-50g €125
-100g €235

🎩DRY CILINDRO🎩
🔴scontato x oggi🔴
-5g €35
-10g €60
-25g €135
-50g €280
-100g €530

🎁regalo per chi passa al meet🎁

CANALE RECENSIONI
https: https://t.me/+iJgKUaE3oUoyM2Y0

UNICO CONTATTO @farmexpress

CANALE CON ORARI E VIDEO✅
https://t.me/+qVbZb7V6nBkxZGRk'''

# Replace the value below with the interval in seconds between each message
interval = 60

async def spam_groups():
    while True:
        for group_username in group_usernames:
            await client.send_message(group_username, message)
        await asyncio.sleep(interval)

@client.on(events.NewMessage(chats=group_usernames))
async def handler(event):
    # Ignore messages sent by the userbot itself
    if event.sender_id == client.uid:
        return

    # Send the message
    for group_username in group_usernames:
        await client.send_message(group_username, message)

# Start the userbot
async def main():
    await client.start()
    await spam_groups()

asyncio.run(main())
