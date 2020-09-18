import re
import random
import vk_api 
import time 
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token='33ff58dd898f929c9b6b9004a7f45d0c38be75f94b0da1c88cc926a80e7da325e4c3bd1a787f7eada7bbe')#ключ сообщества(без звёздочек)
longpoll = VkBotLongPoll(vk_session, '190486942')#id сообщества(положительное число, например


for event in longpoll.listen():
    mesenges = vk_session. method('messages.getConversations', {'offset':0, 'count':20, 'filter':'unanswered'})


    if event.type == VkBotEventType.MESSAGE_NEW:

        body = event.obj.text
        idd_chat = event.obj.peer_id
        idd_man = event.obj.from_id

        
        
        #if body == 'Понял':
        try:
            fio = vk_session.method('users.get',{'user_ids':idd_man})[0]['first_name'] + ' ' + vk_session.method('users.get',{'user_ids':idd_man})[0]['last_name']
            vk_session.method('messages.send',{'peer_id':idd_chat,'random_id':0,'message':fio+':\n\n'+body})
            print(event.obj)
        except:
            print(event.obj)
