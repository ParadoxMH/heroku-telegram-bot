
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

text_AmbasadorProgram = '🔊 Ambasador program'
text_OfficialLinks = '🌐 Official links'
text_FAQ = '🚀 FAQ'

text_Twitter = 'Twitter'
text_Discord = 'Discord'
text_OfficialSite = 'Official site'
text_OtherLinks = 'Other links'
logger = logging.getLogger(__name__)
TOKEN = '5117226938:AAEQj0XxRK8jh46qV2H4BoCuaVFYR8xFBI8'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    keyboard = [
        [
            KeyboardButton(text_AmbasadorProgram, callback_data='1'),
            KeyboardButton(text_OfficialLinks, callback_data='2'),
            KeyboardButton(text_FAQ, callback_data='3'),
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text('Hi, ' + update.message.from_user['first_name'] + '!\n\
I’m PlanetQuest FAQ Bot driven by community.\
You can ask me about PlanetQuest’s aim and main protocol features. Enjoy!', reply_markup=reply_markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def text(update, context):
    keyboard = [
        [
            KeyboardButton(text_AmbasadorProgram, callback_data='1'),
            KeyboardButton(text_OfficialLinks, callback_data='2'),
            KeyboardButton(text_FAQ, callback_data='3'),
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    if(update.message.text == text_AmbasadorProgram):
        update.message.reply_text('https://medium.com/@planetquestgame/introducing-the-community-explorers-ambassador-program-ed68ba92d93e', reply_markup=reply_markup)
    elif(update.message.text == text_OfficialLinks):
        keyboard = [
            [
                InlineKeyboardButton(text_Twitter, url='https://twitter.com/JoinPlanetQuest'),
                InlineKeyboardButton(text_Discord, url='https://discord.gg/planetquest')
            ],
            [InlineKeyboardButton(text_OfficialSite, url='https://planetquest.io/')],
            [InlineKeyboardButton(text_OtherLinks, url='https://linktr.ee/PlanetQuest')],
        ]  
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('What link do you need?', reply_markup=reply_markup)

    elif(update.message.text == text_FAQ):
        update.message.reply_text('https://medium.com/@sky.skyska.ska/hi-guys-5dc52912d8f2', reply_markup=reply_markup) 
    
    else:
        update.message.reply_text('⁉️ Unknown command. Please, press one of buttons below.', reply_markup=reply_markup)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, text))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot    
    #updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://morning-basin-98071.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()