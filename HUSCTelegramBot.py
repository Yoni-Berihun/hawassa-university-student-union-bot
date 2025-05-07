from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)
from dotenv import load_dotenv
import os
import mainMenu, buttonHandler, messageHandler
load_dotenv()

token: Final = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))
SIDAMA_OROMO_ADMIN_CHAT_ID= int(os.getenv('SIDAMA_OROMO_ADMIN_CHAT_ID'))

if not token or not ADMIN_CHAT_ID:
    raise EnvironmentError("BOT_TOKEN or ADMIN_CHAT_ID not set in the environment.")

#---------------------- START COMMAND----------------------------------------
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
#----------------------CHECKS IF THE USER HAS ALREADY CHOSEN A LANGUAGE IF YES IT ONLY DISPLAYS THE MAIN MENU----------------------------------------    
    if not context.user_data.get('language'):
        await language_menu(update,context)
    else:
        await mainMenu.show_main_menu(update, context)

#---------------------- LANGUAGE COMMAND----------------------------------------
async def change_language(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await language_menu(update,context)

#---------------------- DISPLAYS THE LANGUAGE MENU----------------------------------------
async def language_menu(update:Update, context:ContextTypes.DEFAULT_TYPE):
    language_buttons = [
            [InlineKeyboardButton('አማርኛ', callback_data='lang_amharic')],
            [InlineKeyboardButton('English', callback_data='lang_english')],
            [InlineKeyboardButton('Afan Oromo', callback_data='lang_oromia')],
            [InlineKeyboardButton(' Sidaamu Afoo', callback_data='lang_sidama')]
        ]
    await update.message.reply_text(
        "🌍 Please select your preferred language:",
        reply_markup=InlineKeyboardMarkup(language_buttons)
    )
        

#----------------------HANDLES ERRORS AND LOGS THEM TO THE CONSOLE FOR DEBUGGING----------------------------------------
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import traceback
    print(f"Exception caught:\n{traceback.format_exc()}")

#----------------------MAIN----------------------------------------
# IF THE FILE IS DIRECTLY RUN AND NOT IMPORTED
if __name__ == '__main__':
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('language',change_language))
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(buttonHandler.button_handle))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messageHandler.message_handle))
    app.add_error_handler(error)
    print("Polling...")
    app.run_polling()
