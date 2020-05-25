from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, LoginUrl

def forwarded_message(bot, update):
    chat_id = update.message
    #print(bot.forward_message(chat_id=chat_id.chat_id, from_chat_id = '@akhbarefori', message_id = 16))
    print(chat_id.text)


def contact_callback(bot, update):
    contact = update.effective_message.contact
    phone = contact.phone_number
    bot.send_message(chat_id = '@tbottesting', text = phone)
    print(contact)

def contact (bot, update):
    chat_id = update.message
    location_keyboard = KeyboardButton(text="share phone number", request_contact=True)
    custom_keyboard = [[location_keyboard]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
    bot.send_message(chat_id=chat_id.chat_id,
                     text="Share Your Phone number",
                     reply_markup=reply_markup)

def main():
    updater = Updater('1198545285:AAFU2gRL3OuZ7FpDgLQVwfi51uVoGagawc8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('contact', contact))
    #dp.add_handler(CommandHandler('for', forwarded_message))
    dp.add_handler(MessageHandler(Filters.contact, contact_callback))
    dp.add_handler(MessageHandler(Filters.forwarded, forwarded_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
