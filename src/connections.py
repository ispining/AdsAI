from pyrogram import Client
api_id = 21194050 
api_hash = "ef8c398ae656ae51e585e405d3e83ff2"                     
tg = Client("Main", api_id, api_hash)
tg.start()


def get_chat_messages(chat_id):                                       
    return tg.get_chat_history(chat_id)


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


