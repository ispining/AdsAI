from pyrogram import Client
api_id = 21194050 
api_hash = "ef8c398ae656ae51e585e405d3e83ff2"                     
sender_app = Client("Main", api_id, api_hash)                     
sender_app.start()                                             

def get_chat_messages(chat_id):                                       
    with sender_app as bot:                                               
        return bot.get_chat_history(chat_id)                  
  
def send_message(chat_id, message, photo=None):                     
    with sender_app as bot:                                      
        if photo:                                         
            bot.send_photo(chat_id, photo, caption=message)          
        else:                                                   
            bot.send_message(chat_id, message)                             

def my_chats(types=["private", "group", "supergroup"]):       
    result = []                                                
    for dialog in sender_app.get_dialogs():                        
        if dialog.chat.type.value in types:                                 
            result.append({                                     
                "id": dialog.chat.id,                   
                "type": dialog.chat.type.value,                        
                "title": dialog.chat.title,                  
                "username": dialog.chat.username,                 
                "members_count": dialog.chat.members_count})              
    return result


