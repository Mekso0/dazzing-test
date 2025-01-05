import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '7272558954:AAE90stHGOyAvfZ_xHBF4eBiJljXodBInBY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    
    # Отправляем гифку
    with open('seal.gif', 'rb') as gif_file:  # Замените 'seal.gif' на путь к вашей гифке
        bot.send_animation(chat_id, gif_file, caption='🦭 Привет! Это тест бот здесь ничего интересного)')


# Запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)