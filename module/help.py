from telethon import TelegramClient, events, sync
import module.client
client = module.client.client
@events.register(events.NewMessage(pattern=".help"))
async def help(event):
	await event.edit("""

USERBOT 

[01] Bombs - Animation emojise — .bombs
[02] Help - Help menu — .help
[03] Loading  - Animation loading — .loading
[04] Emoji  -  Emoji text editor - .emoji <here text>
[05] Typer - Animation write text - .type <here text>
[06] Lul - animatsia lul - .lul
[07] Snake - Snake animation - .snake 
[08] Nothappy - Abimation Nothappy - .nothappy
[09] Clock - animation clock - .clock
[10] Muah - animation - .muah
[11] Heart - animation - .heart
[12] Gym - animation gymnastic - .gym
[13] Earth - animation globus - .earth
[14] Moon - animation - .moon
[15] Candy - Animatiln - .candy
[16] Smoon - animation - .smoon
[17] Tmoon - animation - .tmoon
[18] Clown - animation - .clown
[19] Star - batterfly and star animation - .star
[20] Boxs - Color animation - .boxs
[21] Rain - water animation - .rain
[22] Clol - "What?" snimation - .clol
[23] Odra - Animation - .odra 
[24] Fleaveme - animation - .fleaveme
[25] Loveu - love animation - .loveu
[26] Plane - animation - .plane
[27] Police - animation sirena - .police
[28] Jio - animation - .jio
[29] Solarsystem - animation - .solarsystem
[30] Fuck - Fuck you - .fuck
[31] Tr - Translator - .tr <language code > <reply message>
[32] Userinfo - Username information - .userinfo <reply>
[33] Base64 - encode and decode  text messages - .b64 en <reply text> .b64 de <reply encoded message>
[34] Snow - animation snow - .snow

Programmer - @dasturchi_uzb_007
""")
	