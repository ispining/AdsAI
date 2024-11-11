import datetime

from pyrogram import Client
api_id = 21194050 
api_hash = "ef8c398ae656ae51e585e405d3e83ff2"                     
tg = Client("Main", api_id, api_hash)
tg.start()


def get_chat_messages(chat_id):
    result = []
    for message in tg.get_chat_history(chat_id):
        result.append({
            "id": message.id,
            "from_user": {"id": message.from_user.id,
                          "is_bot": message.from_user.is_bot,
                          "is_deleted": message.from_user.is_deleted,
                          "is_scam": message.from_user.is_scam,
                          "is_fake": message.from_user.is_fake,
                          "username": message.from_user.username,
                          "first_name": message.from_user.first_name},
            "date": datetime.datetime.strptime(str(message.date), "%Y-%m-%d %H:%M:%S"),
            "chat": {"id": message.chat.id,
                     "type": message.chat.type.value,
                     "title": message.chat.title,
                     "username": message.chat.username,
                     "members_count": message.chat.members_count,
                     "permissions": {"can_send_messages": message.chat.permissions.can_send_messages,
                                     "can_send_media_messages": message.chat.permissions.can_send_media_messages,
                                     "can_send_other_messages": message.chat.permissions.can_send_other_messages,
                                     "can_send_polls": message.chat.permissions.can_send_polls,
                                     "can_add_web_page_previews": message.chat.permissions.can_add_web_page_previews,
                                     "can_invite_users": message.chat.permissions.can_invite_users},
                     },

            "text": message.text})


def send_message(chat_id, message, photo=None):                     
    if photo:
        tg.send_photo(chat_id, photo, caption=message)
    else:
        tg.send_message(chat_id, message)


def my_chats(types=["private", "group", "supergroup"]):       
    result = []                                                
    for dialog in tg.get_dialogs():
        if dialog.chat.type.value in types:                                 
            result.append({                                     
                "id": dialog.chat.id,                   
                "type": dialog.chat.type.value,                        
                "title": dialog.chat.title,                  
                "username": dialog.chat.username,                 
                "members_count": dialog.chat.members_count})              
    return result


