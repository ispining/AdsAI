from pprint import pprint
from src import connections as conn

selected_group = conn.my_chats(types=["supergroup"])[0]

iter_num = 0
for m_info in conn.get_chat_messages(selected_group["id"]):
    print(m_info)
    print()
    iter_num += 1
    if iter_num == 5:
        break

