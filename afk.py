import asyncio
from telethon import TelegramClient, sync, types, events
import time
import re

api_id = '6614831'
api_hash = '09a89d3e65e24da18ac074948974d35b' 


client = TelegramClient('qzbot', api_id, api_hash)


def afk():
    
    class Status():
        status = 0
    
    class Time():
        tm = 0
        
    
    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        if Status.status == 1:
            await client.send_message(event.chat_id, f'это бот, я сейчас занят, вернусь примерно через {Status.tm} минут')
        else:
            pass
                           
            
    
    
    @client.on(events.NewMessage(pattern='.afk', outgoing=True))
    async def cmd_d(event):
        kl = event.message.to_dict()['message']
        Status.tm = kl[-2:]
        Status.status = 1
        m = await client.send_message(event.chat_id, '- afk-bot started -')
        time.sleep(1)
        await client.delete_messages(event.chat_id, [event.id, m.id])
        local_time = float(Status.tm) * 60
        if Status.status == 1:
            await asyncio.sleep(local_time)
            Status.status = 0
    
        
        
     
 
 
    @client.on(events.NewMessage(pattern='.unafk', outgoing=True))
    async def cmd_s(event):
        Status.status = 0
        m = await client.send_message(event.chat_id, '- afk-bot stopped -')
        time.sleep(1)
        await client.delete_messages(event.chat_id, [event.id, m.id])
        
        
        
def dltmsg():                     # удаление входящих и исходящих сообщений
    class Status():
        status = 0
 
    @client.on(events.NewMessage())
    async def handler(event):
        if Status.status == 1:
            await client.delete_messages(event.sender_id, event.id)
        else:
            pass
 
 
    @client.on(events.NewMessage(pattern='.delete'))
    async def cmd_d(event):
        Status.status = 1
        m = await client.send_message(event.chat_id, '- successfully launched -')
        time.sleep(1)
        await client.delete_messages(event.chat_id, [event.id, m.id])
     
     
 
 
    @client.on(events.NewMessage(pattern='.sdelete'))
    async def cmd_s(event):
        Status.status = 0
        m = await client.send_message(event.chat_id, '- stopped successfully -')
        time.sleep(1)
        await client.delete_messages(event.chat_id, [event.id, m.id])
            
dltmsg()        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



































afk()


client.start()
client.run_until_disconnected()

