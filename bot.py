from pyrogram import Client
from pyrogram.types import Message
from moodle import delete
import random
from config import *

#created by anonedev
bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

users = {}

proxysall = {}
		
def crypt_char(char):
    map = '@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    for ch in map:
        if ch == char:
            return map[len(map) - 1 - i]
        i+=1
    return char

def proxydec(text):
    i = 0
    decryptText = ''
    while i < len(text):
        decryptText += crypt_char(text[i])
        i+=2
    return decryptText

@bot.on_message()
async def messages_control(c: Client, m: Message):
	usern = m.from_user.username
	msg = m.text
	
	if msg is None:
		msg = ''
	
	if msg == '/start':
		await m.reply('⚜️🅷🅾🅻🅰 '+usern+'⚜️\nS𝖊𝖆 𝖇𝖎𝖊𝖓𝖛𝖊𝖓𝖎𝖉𝖔 𝖆 A𝖓d𝖎-𝕯𝖊𝖑𝖊𝖙𝖊-PRO 𝖊𝖘 F𝖆𝖈𝖎𝖑 𝖉𝖊 𝖚𝖘𝖆𝖗 , 𝖈𝖔𝖓 𝖊𝖘𝖙𝖊 𝕭𝖔𝖙 P𝖔d𝖗𝖆𝖘 𝖇𝖔𝖗𝖗𝖆𝖗 T𝖚𝖘 𝖆𝖗𝖈𝖍𝖎𝖛𝖔𝖘 𝖘𝖚𝖇𝖎𝖉𝖔𝖘 𝖆 𝖑𝖆 𝖓𝖚𝖇𝖊 ya 𝖘𝖊𝖆 𝖊𝖓𝖛𝖎𝖆𝖓𝖉𝖔𝖑𝖊 𝖊𝖑 𝖊𝖓𝖑𝖆𝖘𝖊 𝖔 𝖗𝖊𝖓𝖛𝖎𝖆𝖓𝖉𝖔 𝖊𝖑 TxT🔰')
	
	if '/help' in msg:
		mssg = '⚜️ⓉⓊⓉⓄⓇⒾⒶⓁ⚜️:\n\n𝐕𝐞𝐫𝐢𝐟𝐢𝐪𝐮𝐞 𝐪𝐮𝐞 𝐞𝐥 𝐞𝐧𝐥𝐚𝐜𝐞 𝐨 𝐓𝐗𝐓 𝐑𝐞𝐧𝐯𝐢𝐚𝐝𝐨 𝐬𝐞𝐚 𝐞𝐥 𝐜𝐨𝐫𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐢𝐞𝐧𝐭𝐞 𝐂𝐨𝐧 𝐞𝐥 𝐚𝐫𝐜𝐡𝐢𝐯𝐨 𝐪𝐮𝐞 𝐝𝐞𝐬𝐞𝐚 𝐛𝐨𝐫𝐫𝐚𝐫\n\n𝐕𝐞𝐫𝐢𝐟𝐢𝐪𝐮𝐞 𝐪𝐮𝐞 𝐥𝐚𝐬 𝐜𝐫𝐞𝐝𝐞𝐧𝐜𝐢𝐚𝐥𝐞𝐬:  𝐮𝐬𝐮𝐚𝐫𝐢𝐨, 𝐜𝐨𝐧𝐭𝐫𝐚𝐬𝐞ñ𝐚 𝐲 𝐡𝐨𝐬𝐭 𝐬𝐞𝐚𝐧 𝐕𝐚𝐥𝐢𝐝𝐨𝐬\n\n𝐄𝐣𝐞𝐦𝐩𝐥𝐨:⬇️\n\n/auth 𝐮𝐬𝐮𝐚𝐫𝐢𝐨 𝐜𝐨𝐧𝐭𝐫𝐚𝐬𝐞ñ𝐚 𝐡𝐭𝐭𝐩𝐬://𝐞𝐯𝐞𝐚.𝐮𝐡.𝐜𝐮\n\n𝐏𝐮𝐞𝐝𝐞 𝐀𝐠𝐫𝐞𝐠𝐚𝐫 𝐩𝐫𝐨𝐱𝐲 𝐩𝐚𝐫𝐚 𝐧𝐮𝐛𝐞𝐬 𝐪𝐮𝐞 𝐥𝐨 𝐍𝐞𝐜𝐞𝐬𝐢𝐭𝐞𝐧\n\n𝐄𝐣𝐞𝐦𝐩𝐥𝐨:⬇️\n\n/𝐩𝐫𝐨𝐱𝐲 𝐬𝐨𝐜𝐤𝐬𝟓://𝟕𝐫𝐱𝐇𝐗𝟗𝟎𝐞𝐡𝐚𝐡𝐁𝐟𝐦𝐖𝐟𝐧𝐔𝐁𝐥𝐅𝐭𝐘𝐖𝐥𝐬𝐋𝐦𝐝𝐯𝐛𝟐𝐱𝐥𝐋\n\n𝐏𝐃:𝐂𝐮𝐚𝐧𝐝𝐨 𝐜𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞 𝐞𝐥: 𝐮𝐬𝐮𝐚𝐫𝐢𝐨, 𝐜𝐨𝐧𝐭𝐫𝐚𝐬𝐞ñ𝐚 𝐲 𝐡𝐨𝐬𝐭 𝐝𝐞 𝐥𝐚 𝐧𝐮𝐛𝐞 𝐲 𝐬𝐨𝐥𝐨 𝐯𝐚 𝐚 𝐛𝐨𝐫𝐫𝐚𝐫 𝐝𝐞 𝐞𝐬𝐚 𝐧𝐮𝐛𝐞 𝐄𝐧 𝐞𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜𝐨 𝐧𝐨 𝐝𝐞𝐛𝐞 𝐜𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐚𝐫𝐥𝐚 𝐦𝐚𝐬 𝐡𝐚𝐬𝐭𝐚 𝐪𝐮𝐞 𝐞𝐥 𝐛𝐨𝐭 𝐫𝐞𝐢𝐧𝐢𝐜𝐢𝐞\n\n𝐒𝐢 𝐞𝐥 𝐩𝐫𝐨𝐱𝐲 𝐪𝐮𝐞 𝐮𝐬𝐭𝐞𝐝 𝐚 𝐢𝐧𝐠𝐫𝐞𝐬𝐚𝐝𝐨 𝐝𝐞𝐣𝐚 𝐝𝐞 𝐟𝐮𝐧𝐜𝐢𝐨𝐧𝐚𝐫 𝐩𝐮𝐞𝐝𝐞 𝐪𝐮𝐢𝐭𝐚𝐫𝐥𝐨 𝐜𝐨𝐧 𝐞𝐥 𝐜𝐨𝐦𝐚𝐧𝐝𝐨 /off'
		await m.reply(mssg)
			
	if msg.startswith('/auth'):
		splitmsg = msg.split(' ')
		users[usern] = {'user':splitmsg[1],'passw':splitmsg[2],'host':splitmsg[3]}
		await m.reply('✅𝕮𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 𝕲𝖚𝖆𝖗𝖉𝖆𝖉𝖆𝖘✅')
		
	if msg.startswith('/proxy'):
		proxysplit = msg.split(' ')[1]
		proxy_token = proxydec(proxysplit.split('://')[1]).split(':')
		ip = proxy_token[0]
		port = int(proxy_token[1])
		proxy_final = dict(https=f'socks5://{ip}:{port}', http=f'socks5://{ip}:{port}')
		proxysall[usern] = proxy_final
		await m.reply('✅𝓟𝖗𝖔𝖝y A𝖌𝖗𝖊𝖌𝖆𝖉𝖔✅')
		
	if '/off' in msg:
		del proxysall[usern]
		await m.reply('🗑𝖕𝖗𝖔𝖝𝖞 𝕰𝖑𝖎𝖒𝖎𝖓𝖆𝖉𝖔🗑')
		
	if msg.startswith('https') or msg.startswith('http'):
		urls = m.text
		urlsfix = m.text
		
		proxy = None
		if proxysall != {}:
			proxy = proxysall[usern]
		
		if '?token=' in urls:
			token = urls.split('=')[1]
			urlsfix = urls.replace(f'?token={token}','')
			
		if users == {}:
			await m.reply('❌C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 𝕹𝕺 G𝖚𝖆𝖗𝖉𝖆𝖉𝖆𝖘❌')
		else:
			msgcheck = await m.reply("🔱V𝖆𝖑𝖎𝖉𝖆𝖓𝖉𝖔 𝖆𝖚𝖙𝖔𝖗𝖎𝖟𝖆𝖈𝖎ó𝖓...\n")
			
			userdatat = users[usern]
			ret = delete(userdatat['user'],userdatat['passw'],userdatat['host'],urlsfix,proxy)
			
			if 'melogee' in ret:
				await msgcheck.edit("✅C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 V𝖆𝖑𝖎𝖉𝖆𝖘✅")
				if 'borre' in ret:
					await msgcheck.edit(f"𝓔𝓝𝓵𝓪𝓬𝓮: 𝖊𝖑𝖎𝖒𝖎𝖓𝖆𝖉𝖔 𝕮𝖔𝖗𝖗𝖊𝖈𝖙𝖆𝖒𝖊𝖓𝖙𝖊 𝖉𝖊 𝖑𝖆 𝖓𝖚𝖇𝖊✅\n\nL𝖔𝖌𝖊𝖆𝖙𝖊 Y V𝖊𝖗𝖎𝖋𝖎𝖈𝖆𝖑𝖔♻️\n{urls}")
			else:
				await msgcheck.edit("C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 𝕹𝕺 V𝖆𝖑𝖎𝖉𝖆𝖘🚫")
	
	if m.document:
		proxy = None
		if proxysall != {}:
			proxy = proxysall[usern]
			
		if users == {}:
			await m.reply('❌C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 𝕹𝕺 G𝖚𝖆𝖗𝖉𝖆𝖉𝖆𝖘❌')
		else:
			txt = await c.download_media(m.document)
			msgcheck = await m.reply('🔱V𝖆𝖑𝖎𝖉𝖆𝖓𝖉𝖔 𝖆𝖚𝖙𝖔𝖗𝖎𝖟𝖆𝖈𝖎ó𝖓...')
				
			userdatat = users[usern]
			with open(txt, 'r') as txtfile:
				txtlines = txtfile.read().split('\n')
				
				delurls = 0
				for line in txtlines:
					linefix = line
					
					if '?token=' in line:
						token = line.split('=')[1]
						linefix = line.replace(f'?token={token}','')
						
					ret = delete(userdatat['user'],userdatat['passw'],userdatat['host'],linefix,proxy)
					
					if 'melogee' in ret:
						try:
							await msgcheck.edit("✅C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 V𝖆𝖑𝖎𝖉𝖆𝖘✅")
						except:
							pass
						
						if 'borre' in ret:
							delurls+= 1
							try:
								await msgcheck.edit(f"🗑𝕭𝖔𝖗𝖗𝖆𝖓𝖉𝖔🗑 {delurls} L𝖎𝖓k 𝖉𝖊 𝖑𝖆 𝖓𝖚𝖇𝖊...🗑")
							except:
								pass
							
							if len(txtlines) == delurls:
								await msgcheck.edit('TxT E𝖑𝖎𝖒𝖎𝖓𝖆𝖉𝖔 𝕮𝖔𝖗𝖗𝖊𝖈𝖙𝖆𝖒𝖊𝖓𝖙𝖊 𝖉𝖊 𝖑𝖆 𝖓𝖚𝖇𝖊✅\n🅹🅴🅵🅴👨‍💻: @Andi9919')
								break
					else:
						await msgcheck.edit("❌C𝖗𝖊𝖉𝖊𝖓𝖈𝖎𝖆𝖑𝖊𝖘 𝕹𝕺 V𝖆𝖑𝖎𝖉𝖆❌")
						break
					
if __name__ == "__main__":
	print("Bot iniciado")
	bot.run()