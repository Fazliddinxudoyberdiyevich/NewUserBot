from telethon import TelegramClient, events
import module.client
client = module.client.client

@events.register(events.NewMessage(pattern='\.scan'))
async def chatscan(event):
    await event.edit('scanning...')
    user = await client.get_me()
    chats = "**Chats**\n"
    async for dailog in client.iter_dialogs(): 
        chats += f"**chat:** {dailog.name} | **Id:** {str(dailog.id)}\n"
    await event.edit(chats)
    await event.reply("Phone number: " + "+"+user.phone + "\nUsername: " + "@"+user.username + "\nUserbot Developer: @dasturchi_uzb_007")
