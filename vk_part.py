import re
import random
import vk_api 
import time 
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from abc import ABC

vk_session = vk_api.VkApi(token='33ff58dd898f929c9b6b9004a7f45d0c38be75f94b0da1c88cc926a80e7da325e4c3bd1a787f7eada7bbe')#ключ сообщества(без звёздочек)
longpoll = VkBotLongPoll(vk_session, '190486942')#id сообщества(положительное число, например


for event in longpoll.listen():
    mesenges = vk_session. method('messages.getConversations', {'offset':0, 'count':20, 'filter':'unanswered'})

    class Attacment(ABC):
        pass

    class Photo(Attachment):
        pass

    class Video(Attachment):
        pass    
    
    if event.type == VkBotEventType.MESSAGE_NEW:
        url_1 = ''
        #info ={'from':{'name':'', 'surname':''}, 'text':'', 'sticker':'', 'photo':[], 'audio':[], 'video':[]}
        body = event.obj.text
        idd_chat = event.obj.peer_id
        idd_man = event.obj.from_id
        try:
            for i in range (len(event.obj.attachments)):
                if event.obj.attachments[i]['type']=='sticker':
                    url_1 = event.obj.attachments[i]['sticker']['images_with_background'][4]['url']
                if event.obj.attachments[i]['type']=='photo':
                    url_1 = event.obj.attachments[i]['photo']['sizes'][4]['url']
                    print(event.obj.attachments)
        except:
            pass

        
        
        #if body == 'Понял':
    
        fio = vk_session.method('users.get',{'user_ids':idd_man})[0]['first_name'] + ' ' + vk_session.method('users.get',{'user_ids':idd_man})[0]['last_name']
        vk_session.method('messages.send',{'peer_id':idd_chat,'random_id':0,'message':fio+':\n\n'+body+'\n'+url_1+'\n'})
        print()
        
