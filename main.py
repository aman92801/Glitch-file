from telebot import TeleBot, types
from keep_alive import keep_alive
import os

keep_alive()

bot = TeleBot(os.environ['BOT_TOKEN'])

bot_username = "Freeesubsbot"  # Replace with your actual bot username without @

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    verify_btn = types.InlineKeyboardButton("ðŸ” Verify Now", url="https://link-target.net/your-link")
    markup.add(verify_btn)
    bot.send_message(message.chat.id, "ðŸš€ Welcome! Please complete verification.", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if "youtube.com/" in message.text or "youtu.be/" in message.text:
        markup = types.InlineKeyboardMarkup()
        share_btn = types.InlineKeyboardButton(
            "ðŸ“¤ Share with Friends",
            url=f"https://wa.me/?text=ðŸŽ Get%20Free%20YouTube%20Subscribers!%0AðŸ‘‰%20Use%20this%20bot:%20https://t.me/{Freeesubsbot}"
        )
        markup.add(share_btn)
        bot.send_message(message.chat.id, "âœ… Done! Subscribers on the way!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "â— Please enter a valid YouTube link.")

bot.infinity_polling()
