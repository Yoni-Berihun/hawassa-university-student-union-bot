from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    english_choice_buttons = [
        [InlineKeyboardButton('Complaint ⚠️', callback_data='complaint')],
         [InlineKeyboardButton('Suggestion 💡', callback_data='suggestion')]
    ]
    amharic_choice_buttons = [
        [InlineKeyboardButton('ቅሬታ ⚠️', callback_data='complaint')],
         [InlineKeyboardButton('አስተያየት 💡', callback_data='suggestion')]
    ]
    sidama_choice_buttons = [
        [InlineKeyboardButton('koffeenya ⚠️', callback_data='complaint')],
         [InlineKeyboardButton('Hedi-woro 💡', callback_data='suggestion')]
    ]
    oromia_choice_buttons = [
        [InlineKeyboardButton('Komii ⚠️', callback_data='complaint')],
         [InlineKeyboardButton('Yaada 💡', callback_data='suggestion')]
    ]
    

    if context.user_data['language']=='english':
        await update.message.reply_text(
            "Hello!👋\nThank you for reaching out to the Hawassa University Feedback Bot!\nWe're here to listen to your feedback.\nWhat would you like to share today?",
            reply_markup=InlineKeyboardMarkup(english_choice_buttons)
        )

    elif context.user_data['language']=='sidama':
        await update.message.reply_text(
            "Hello!👋\nHawaasi Yuniversite tumi-qolote barera afantinoonni daafira galateemmo!\nYuniversite uytannohe owaante lainohunni heedhannohe hedonna koffeenya buuxate shinqoommo.\nTecho ninke ledo mayinni xaadate dayitto/a?", 
            reply_markup=InlineKeyboardMarkup(sidama_choice_buttons)
        )

    elif context.user_data['language']=='oromia':
        await update.message.reply_text(
            "Baga gara booti hawwaasa yaadni itti kennamutti nagaan dhuftan! 👋\nBootin kun yaada keessan komii fi ilaalcha qabdan  karaa nagaa isaa eeggateen gara qaama dhimmi isaa ilaallatutti  biraan ga'uuf isin gargaara!\nHar'a nutti maal dubbachuu barbaaddan?", 
            reply_markup=InlineKeyboardMarkup(oromia_choice_buttons)
        )

    elif context.user_data['language']=='amharic':
        await update.message.reply_text(
            "ሰላም!👋 \nእንኳን ወደ ሃዋሳ ዩኒቨርሲቲ አስተያየት መስጫ ቦት በሰላም መጡ!\nይህ ቦት ሃሳብዎን አስተያየትዎን እና ቅሬታዎን ደህንነቶን በጠበቀ መልኩ ለሚመለከታቸው አካላት ለማድረስ ያግዝዎታል!\nዛሬ ለእኛ ምን መናገር ይፈልጋሉ?", 
            reply_markup=InlineKeyboardMarkup(amharic_choice_buttons)
        )

    else:
        await update.message.reply_text(
            "Sorry something went wrong. Please restart the bot by using the /start command."
        )