# @saddys0 my telegram, feel free to dm me

from telethon import TelegramClient, events
import asyncio

# Replace the values below with your own API ID, API hash, and session name
api_id = enter api id
api_hash = 'enter api hash'
session_name = 'your_session_name'

client = TelegramClient(session_name, api_id, api_hash)

# Replace the values below with the usernames of the groups you want to target
group_usernames = ['@entergroup1', '@entergroup2']

# Replace the value below with the message you want to send
message = 'enter your msg'

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
