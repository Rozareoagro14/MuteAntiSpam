from pyrogram import Client, filters
from time import sleep

app = Client("my_account")

# Идентификатор пользователя, от которого вы хотите отключать уведомления
target_user_id = 123456789

# Идентификатор чата, от которого вы хотите отключать уведомления
target_chat_id = -100123456789  # Замените на фактический идентификатор чата

@app.on_message(filters.user(target_user_id))
def handle_message(_, message):
    # Отключаем уведомления на 15 секунд
    app.mute_chat(chat_id=target_chat_id, until_date=int(message.date) + 15)

    # Ваш код обработки сообщения здесь

    # Ждем 15 секунд
    sleep(15)

    # Включаем уведомления
    app.unmute_chat(chat_id=target_chat_id)

app.run()
