from telethon import TelegramClient, events, sync
from time import gmtime, strftime
from emoji import emojize
import asyncio
import os, sys

import module.client, module.url, module.scan,  module.bombs,  module.help,  module.loading,  module.emoji, module.type,  module.magicrun,  module.animation,  module.animation2, module.mute, module.fuck,  module.tr,  module.userinfo,  module.base64, module.snow
#
client = module.client.client
client.add_event_handler(module.bombs.bombs)
client.add_event_handler(module.help.help) 
client.add_event_handler(module.loading.loading) 
client.add_event_handler(module.emoji.itachi) 
client.add_event_handler(module.type.type) 
client.add_event_handler(module.magicrun.magicrun) 	
client.add_event_handler(module.animation.lul)
client.add_event_handler(module.animation.snake)
client.add_event_handler(module.animation.nothappy)
client.add_event_handler(module.animation.clock)
client.add_event_handler(module.animation.muah)
client.add_event_handler(module.animation.heart)	
client.add_event_handler(module.animation.gym)
client.add_event_handler(module.animation.earth)
client.add_event_handler(module.animation.moon)
client.add_event_handler(module.animation.candy)
client.add_event_handler(module.animation.smoon)
client.add_event_handler(module.animation.tmoon)
client.add_event_handler(module.animation.clown)
client.add_event_handler(module.animation2.star)
client.add_event_handler(module.animation2.boxs)		
client.add_event_handler(module.animation2.rain)
client.add_event_handler(module.animation2.clol)
client.add_event_handler(module.animation2.odra)
client.add_event_handler(module.animation2.fleaveme)		
client.add_event_handler(module.animation2.loveu)
client.add_event_handler(module.animation2.plane)
client.add_event_handler(module.animation2.police)
client.add_event_handler(module.animation2.jio)		
client.add_event_handler(module.animation2.solarsystem)
client.add_event_handler(module.mute.mute)		
client.add_event_handler(module.fuck.fuck)
client.add_event_handler(module.tr.tr)
client.add_event_handler(module.userinfo.userinfo)
client.add_event_handler(module.base64.runb64)
client.add_event_handler(module.snow.snow)		
client.add_event_handler(module.scan.chatscan)	
client.add_event_handler(module.url.runus)	

	

client.start()
os.system("clear")
print("""\033[031m
██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║███████╗█████╗  ██████╔╝██████╔╝██║   ██║   ██║   
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   
╚██████╔╝███████║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   

\033[032mUSERBOT STARTED""")

client.run_until_disconnected()