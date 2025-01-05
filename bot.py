import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7272558954:AAE90stHGOyAvfZ_xHBF4eBiJljXodBInBY'  # ВНИМАНИЕ: лучше хранить токен вне кода (см. "Альтернативы")
bot = telebot.TeleBot(BOT_TOKEN)

# Путь к файлу с GIF
GIF_PATH = 'gif_file.gif'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    try:
      with open(GIF_PATH, 'rb') as gif:
          bot.send_animation(chat_id, gif, caption="🦭 Привет! Это тест бот здесь ничего интересного)")
    except FileNotFoundError:
       bot.send_message(chat_id, 'Ошибка: GIF файл не найден')
    except Exception as e:
       bot.send_message(chat_id, f"Произошла ошибка: {e}")
    
if __name__ == '__main__':
    print('Бот запущен...')
    bot.polling(none_stop=True)