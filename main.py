
import os
import telebot
import time

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот работает. Следим за новыми токенами! 💣")

def run():
    while True:
        # Тут можно будет вставить сканер или API DexTools и т.п.
        # Сейчас просто отправляет сообщение раз в час
        bot.send_message(CHAT_ID, "Пример уведомления: новый токен найден!")
        time.sleep(3600)

if __name__ == "__main__":
    bot.polling(none_stop=True)

