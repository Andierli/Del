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
		await m.reply('âï¸ð·ð¾ð»ð° '+usern+'âï¸\nSðð ðððððððððð ð Aðdð-ð¯ððððð-PRO ðð Fðððð ðð ðððð , ððð ðððð ð­ðð Pðdððð ðððððð Tðð ðððððððð ððððððð ð ðð ðððð ya ððð ðððððððððð ðð ðððððð ð ððððððððð ðð TxTð°')
	
	if '/help' in msg:
		mssg = 'âï¸ââââââ¾â¶ââï¸:\n\nððð«ð¢ðð¢ðªð®ð ðªð®ð ðð¥ ðð§ð¥ððð ð¨ ððð ððð§ð¯ð¢ððð¨ ð¬ðð ðð¥ ðð¨ð«ð«ðð¬ð©ð¨ð§ðð¢ðð§ð­ð ðð¨ð§ ðð¥ ðð«ðð¡ð¢ð¯ð¨ ðªð®ð ððð¬ðð ðð¨ð«ð«ðð«\n\nððð«ð¢ðð¢ðªð®ð ðªð®ð ð¥ðð¬ ðð«ðððð§ðð¢ðð¥ðð¬:  ð®ð¬ð®ðð«ð¢ð¨, ðð¨ð§ð­ð«ðð¬ðÃ±ð ð² ð¡ð¨ð¬ð­ ð¬ððð§ ððð¥ð¢ðð¨ð¬\n\nðð£ðð¦ð©ð¥ð¨:â¬ï¸\n\n/auth ð®ð¬ð®ðð«ð¢ð¨ ðð¨ð§ð­ð«ðð¬ðÃ±ð ð¡ð­ð­ð©ð¬://ðð¯ðð.ð®ð¡.ðð®\n\nðð®ððð ðð ð«ðð ðð« ð©ð«ð¨ð±ð² ð©ðð«ð ð§ð®ððð¬ ðªð®ð ð¥ð¨ ððððð¬ð¢ð­ðð§\n\nðð£ðð¦ð©ð¥ð¨:â¬ï¸\n\n/ð©ð«ð¨ð±ð² ð¬ð¨ðð¤ð¬ð://ðð«ð±ðððððð¡ðð¡ððð¦ððð§ððð¥ðð­ððð¥ð¬ðð¦ðð¯ððð±ð¥ð\n\nðð:ðð®ðð§ðð¨ ðð¨ð§ðð¢ð ð®ð«ð ðð¥: ð®ð¬ð®ðð«ð¢ð¨, ðð¨ð§ð­ð«ðð¬ðÃ±ð ð² ð¡ð¨ð¬ð­ ðð ð¥ð ð§ð®ðð ð² ð¬ð¨ð¥ð¨ ð¯ð ð ðð¨ð«ð«ðð« ðð ðð¬ð ð§ð®ðð ðð§ ðð¬ð©ððð¢ðð¢ðð¨ ð§ð¨ ðððð ðð¨ð§ðð¢ð ð®ð«ðð«ð¥ð ð¦ðð¬ ð¡ðð¬ð­ð ðªð®ð ðð¥ ðð¨ð­ ð«ðð¢ð§ð¢ðð¢ð\n\nðð¢ ðð¥ ð©ð«ð¨ð±ð² ðªð®ð ð®ð¬ð­ðð ð ð¢ð§ð ð«ðð¬ððð¨ ððð£ð ðð ðð®ð§ðð¢ð¨ð§ðð« ð©ð®ððð ðªð®ð¢ð­ðð«ð¥ð¨ ðð¨ð§ ðð¥ ðð¨ð¦ðð§ðð¨ /off'
		await m.reply(mssg)
			
	if msg.startswith('/auth'):
		splitmsg = msg.split(' ')
		users[usern] = {'user':splitmsg[1],'passw':splitmsg[2],'host':splitmsg[3]}
		await m.reply('âð®ððððððððððð ð²ððððððððâ')
		
	if msg.startswith('/proxy'):
		proxysplit = msg.split(' ')[1]
		proxy_token = proxydec(proxysplit.split('://')[1]).split(':')
		ip = proxy_token[0]
		port = int(proxy_token[1])
		proxy_final = dict(https=f'socks5://{ip}:{port}', http=f'socks5://{ip}:{port}')
		proxysall[usern] = proxy_final
		await m.reply('âððððy Aðððððððâ')
		
	if '/off' in msg:
		del proxysall[usern]
		await m.reply('ðððððð ð°ððððððððð')
		
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
			await m.reply('âCððððððððððð ð¹ðº Gððððððððâ')
		else:
			msgcheck = await m.reply("ð±Vðððððððð ððððððððððÃ³ð...\n")
			
			userdatat = users[usern]
			ret = delete(userdatat['user'],userdatat['passw'],userdatat['host'],urlsfix,proxy)
			
			if 'melogee' in ret:
				await msgcheck.edit("âCððððððððððð Vððððððâ")
				if 'borre' in ret:
					await msgcheck.edit(f"ðððµðªð¬ð®: ððððððððð ð®ðððððððððððð ðð ðð ððððâ\n\nLðððððð Y Vðððððððððâ»ï¸\n{urls}")
			else:
				await msgcheck.edit("Cððððððððððð ð¹ðº Vððððððð«")
	
	if m.document:
		proxy = None
		if proxysall != {}:
			proxy = proxysall[usern]
			
		if users == {}:
			await m.reply('âCððððððððððð ð¹ðº Gððððððððâ')
		else:
			txt = await c.download_media(m.document)
			msgcheck = await m.reply('ð±Vðððððððð ððððððððððÃ³ð...')
				
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
							await msgcheck.edit("âCððððððððððð Vððððððâ")
						except:
							pass
						
						if 'borre' in ret:
							delurls+= 1
							try:
								await msgcheck.edit(f"ðð­ðððððððð {delurls} Lððk ðð ðð ðððð...ð")
							except:
								pass
							
							if len(txtlines) == delurls:
								await msgcheck.edit('TxT Eðððððððð ð®ðððððððððððð ðð ðð ððððâ\nð¹ð´ðµð´ð¨âð»: @Andi9919')
								break
					else:
						await msgcheck.edit("âCððððððððððð ð¹ðº Vðððððâ")
						break
					
if __name__ == "__main__":
	print("Bot iniciado")
	bot.run()