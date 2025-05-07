from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))
SIDAMA_OROMO_ADMIN_CHAT_ID = int(os.getenv('SIDAMA_OROMO_ADMIN_CHAT_ID'))

async def detail_theft(update: Update, context: ContextTypes.DEFAULT_TYPE, step: int, owner: str):
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message

    context.user_data['message_step'] = step

    if step == 1:
        if context.user_data['language'] == 'english':
            await message.reply_text('Please enter the name of the item that was lost ✍️')
        elif context.user_data['language'] == 'amharic':
            await message.reply_text('እባክዎ የተሰረቀውን ንብረት ስም ይጻፉልን ✍️')
        elif context.user_data['language'] == 'sidama':
            await message.reply_text('Mooramino jajji/uduunnichi dana borreessi ✍️')
        elif context.user_data['language'] == 'oromia':
            await message.reply_text('Maqaa qabeenya hatamee barreess ✍️')                
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

    elif step == 2:
        if context.user_data['language'] == 'english':
            if context.user_data['theft_owner'] == 'own':
                await message.reply_text('Please enter your full name ✍️')
            else:
                await message.reply_text('Please enter the name of the person that lost the item ✍️')
        elif context.user_data['language'] == 'amharic':
            if context.user_data['theft_owner'] == 'own':
                await message.reply_text('እባክዎ ሙሉ ስምዎን ይጻፉልን✍️')
            else:
                await message.reply_text('እባክዎ የንብረቱን ባለቤት ስም ይጻፉልን ✍️')
        elif context.user_data['language'] == 'sidama':
            if context.user_data['theft_owner'] == 'own':
                await message.reply_text('Su makki ayeati? ✍️')
            else:
                await message.reply_text('Jajju/uduunnichu anni su ma borreessi✍️')
        elif context.user_data['language'] == 'oromia':
            if context.user_data['theft_owner'] == 'own':
                await message.reply_text('Maqaan keessan eenyu jedhama ✍️')
            else:
                await message.reply_text('Maqaa abbaa qabeenyaa asitti barreessaa ✍️')
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

    elif step == 3:
        english_button = [
            [InlineKeyboardButton('Dorm', callback_data='location_dorm')],
            [InlineKeyboardButton('Library', callback_data='location_library')],
            [InlineKeyboardButton('Other', callback_data='location_other')]
        ]
        amharic_button = [
            [InlineKeyboardButton('ዶርም', callback_data='location_dorm')],
            [InlineKeyboardButton('ላይብረሪ', callback_data='location_library')],
            [InlineKeyboardButton('ሌላ ቦታ', callback_data='location_other')]
        ]
        oromia_button = [
            [InlineKeyboardButton('Doormii', callback_data='location_dorm')],
            [InlineKeyboardButton('Layibrarii', callback_data='location_library')],
            [InlineKeyboardButton('Kan biroo', callback_data='location_other')]
        ]
        sidama_button = [
            [InlineKeyboardButton('Gallanniwa/dormete', callback_data='location_dorm')],
            [InlineKeyboardButton('Maxaaffate mine', callback_data='location_library')],
            [InlineKeyboardButton('Wolewa', callback_data='location_other')]
        ]
        
        if context.user_data['language'] == 'english':
            reply_markup = InlineKeyboardMarkup(english_button)
            await message.reply_text('Where was the item stolen from?', reply_markup=reply_markup)
        elif context.user_data['language'] == 'amharic':
            reply_markup = InlineKeyboardMarkup(amharic_button)
            await message.reply_text('ንብረቱ የተሰረቀበትን ቦታ ስም ይጻፉልን', reply_markup=reply_markup)
        elif context.user_data['language'] == 'sidama':
            reply_markup = InlineKeyboardMarkup(sidama_button)
            await message.reply_text('Jajju/uduunnichu mooramino base mamaati?', reply_markup=reply_markup)
        elif context.user_data['language'] == 'oromia':
            reply_markup = InlineKeyboardMarkup(oromia_button)
            await message.reply_text('Qabeenyi eessaa hatame?', reply_markup=reply_markup)
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
    
    elif step == 4:
        theft_location = context.user_data['theft_location']

        if theft_location == 'dorm':
            if context.user_data['language'] == 'english':
                await message.reply_text('Please enter your block and dorm number ✍️')
            elif context.user_data['language'] == 'amharic':
                await message.reply_text('እባክዎ ንብረቱ የተሰረቀበትን ብሎክ እና የዶርም ቁጥር ያስገቡ✍️')
            elif context.user_data['language'] == 'sidama':
                await message.reply_text('Galatto/a ijaarinna waalchu kiiro borreessi ✍️')
            elif context.user_data['language'] == 'oromia':
                await message.reply_text('Lakkofsa Bilookii keessani fi doormii keessani barreessa ✍️')
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
         
        elif theft_location == 'library':
            if context.user_data['language'] == 'english':
                await message.reply_text('Please enter the date and time ✍️')
            elif context.user_data['language'] == 'amharic':
                await message.reply_text('እባክዎ ንብረቱ የተሰረቀበትን ቀን እና ሰአት ያስገቡ✍️')
            elif context.user_data['language'] == 'sidama':
                await message.reply_text('Jajju/uduunnichu moorami barranna saate borreessi ✍️')
            elif context.user_data['language'] == 'oromia':
                await message.reply_text('Maaloo yeroo fi guyyaa mi\'i  hatame adda baasa ✍️')
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
        
        elif theft_location == 'other':
            if context.user_data['language'] == 'english':
                await message.reply_text('Please enter where the theft occurred ✍️')
            elif context.user_data['language'] == 'amharic':
                await message.reply_text('እባክዎ ንብረቱ የተሰረቀበትን ቦታ ያስገቡ✍️')
            elif context.user_data['language'] == 'sidama':
                await message.reply_text('Moorami  baycho borreessi ✍️')
            elif context.user_data['language'] == 'oromia':
                await message.reply_text('Iddoo adda baasa ibsaa yeroo qabeenyichi hatamuutti ✍️')
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
    
    elif step == 5:
        theft_location = context.user_data['theft_location']

        if theft_location == 'dorm':
            if context.user_data['language'] == 'english':
                await update.message.reply_text('Please enter the date and time ✍️')
            elif context.user_data['language'] == 'amharic':
                await update.message.reply_text('እባክዎ ንብረቱ የተሰረቀበትን ቀን እና ሰአት ያስገቡ ✍️')
            elif context.user_data['language'] == 'sidama':
                await update.message.reply_text('Jajju/uduunnichu moorami barranna saate borreessi ✍️')
            elif context.user_data['language'] == 'oromia':
                await update.message.reply_text('Maaloo yeroo fi guyyaa mi\'i  hatame adda baasa ✍️')
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

        elif theft_location == 'library':
            if context.user_data['theft_owner'] == 'own':
                admin_message = (
                    f"New report has been filed regarding a stolen item from @{context.user_data['user']}\n\n"
                    f"• Location of Incident: {context.user_data['theft_location']}\n"
                    f"• Item Name: {context.user_data['theft_item']}\n"
                    f"• Name of Reporter: {context.user_data['theft_name']}\n"
                    f"• Reporter is the Owner: {context.user_data['theft_owner']}\n"
                    f"• Date & Time of Incident: {context.user_data['theft_date&time']}\n"
                    f"• Reported to Police: {context.user_data['reported_theft']}\n"
                )
            else:
                admin_message = (
                    f"New report has been filed regarding a stolen item\n\n"
                    f"• Location of Incident: {context.user_data['theft_location']}\n"
                    f"• Item Name: {context.user_data['theft_item']}\n"
                    f"• Name of Reporter: {context.user_data['theft_name']}\n"
                    f"• Reporter is the Owner: {context.user_data['theft_owner']}\n"
                    f"• Date & Time of Incident: {context.user_data['theft_date&time']}\n"
                )

            if context.user_data['language'] == 'english':
                await context.bot.send_message(
                    chat_id=ADMIN_CHAT_ID,
                  message_thread_id=int(os.getenv('THEFT_THREAD_ID')),
                    text=admin_message
                )
                await message.reply_text(
                    'Thank you for your report. ✅ Your report will be reviewed, and appropriate actions will be taken.\n\n'
                    'You can use the following phone number 📞 to follow up on the investigation:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu  – 0913405901 '
                )
            elif context.user_data['language'] == 'amharic':
                await context.bot.send_message(
                    chat_id=ADMIN_CHAT_ID,
                    message_thread_id=int(os.getenv('THEFT_THREAD_ID')),
                    text=admin_message
                )
                await message.reply_text(
                    'ጥቆማዎን ስላቅረቡ እናመሰግናለን ✅ጥቆማዎን በሚገባ ተመልክተን አስፈላጊ እርምጃዎችን እንወስዳለን \n\n'
                    'ጥቆማዎን በሚከተሉት ስልክ ቁጥሮች  📞 በመደወል መከታተል ይችላሉ ፡ \n\n'
                    'እሰይ ጴጥሮስ – 0926435305 \n\n'
                    'ኮማንደር ሃይሉ – 0913405901 '
                )
            elif context.user_data['language'] == 'sidama':
                await context.bot.send_message(
                    chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID,
                    message_thread_id=int(os.getenv('SIDAMA_OROMO_THEFT_THREAD_ID')),
                    text=admin_message
                )
                await message.reply_text(
                    'Waan ripoortii gootaniif guddaa galatooma. ✅ Ripoortiin keessan erga ilaalame booda gochi seera qabeessa ta\'ee ni fudhatama\n'
                    'Adeemsa qorannoo kana duukaa bu\'uuf lakkofsota kana fayyadamu ni dandeessu:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu  0913405901 '
                )
            elif context.user_data['language'] == 'oromia':
                await context.bot.send_message(
                    chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID,
                    message_thread_id=int(os.getenv('SIDAMA_OROMO_THEFT_THREAD_ID')),
                    text=admin_message
                )
                await message.reply_text(
                    'Waan ripoortii gootaniif guddaa galatooma. ✅ Ripoortiin keessan erga ilaalame booda gochi seera qabeessa ta\'ee ni fudhatama\n'
                    'Adeemsa qorannoo kana duukaa bu\'uuf lakkofsota kana fayyadamu ni dandeessu:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu – 0913405901 ' 
                )
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

            keys_to_remove = ('theft_owner', 'theft_name', 'theft_item', 'theft_date&time', 'reported_theft', 'theft_location')
            for key in keys_to_remove:
                context.user_data.pop(key, None)
        
        elif theft_location == 'other':
            if context.user_data['language'] == 'english':
                await update.message.reply_text('Please enter the date and time ✍️')
            elif context.user_data['language'] == 'amharic':
                await update.message.reply_text('እባክዎ ንብረቱ የተሰረቀበትን ቀን እና ሰአት ያስገቡያስገቡ ✍️')
            elif context.user_data['language'] == 'sidama':
                await update.message.reply_text('Jajju/uduunnichu moorami barranna saate borreessi.✍️')
            elif context.user_data['language'] == 'oromia':
                await update.message.reply_text('Maaloo yeroo fi guyyaa mi i  hatame adda baasa✍️')
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

    elif step == 6:
        if context.user_data['theft_owner'] == 'own':
            admin_message = (
                f"New report has been filed regarding a stolen item from @{context.user_data['user']}\n\n"
                f"• Location of Incident: {context.user_data['theft_location']}\n"
                f"• Item Name: {context.user_data['theft_item']}\n"
                f"• Name of Reporter: {context.user_data['theft_name']}\n"
                f"• Reporter is the Owner: {context.user_data['theft_owner']}\n"
                f"• Date & Time of Incident: {context.user_data['theft_date&time']}\n"
                f"• Reported to Police: {context.user_data['reported_theft']}\n"
            )
        else:
            admin_message = (
                f"New report has been filed regarding a stolen item\n\n"
                f"• Location of Incident: {context.user_data['theft_location']}\n"
                f"• Item Name: {context.user_data['theft_item']}\n"
                f"• Name of Reporter: {context.user_data['theft_name']}\n"
                f"• Reporter is the Owner: {context.user_data['theft_owner']}\n"
                f"• Date & Time of Incident: {context.user_data['theft_date&time']}\n"
            )

        if context.user_data['theft_location'] == 'dorm':
            admin_message += f"• Block and Dorm number: {context.user_data['theft_block&dorm']}\n"

        if context.user_data['language'] == 'english':
            await context.bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                message_thread_id=int(os.getenv(f"{context.user_data['complain']}_THREAD_ID")),
                text=admin_message
            )
            await message.reply_text(
                'Thank you for your report. ✅ Your report will be reviewed, and appropriate actions will be taken.\n\n'
                    'You can use the following phone number 📞 to follow up on the investigation:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu  – 0913405901 '

            )
        elif context.user_data['language'] == 'amharic':
            await context.bot.send_message(
                chat_id=ADMIN_CHAT_ID,
                message_thread_id=int(os.getenv(f"{context.user_data['complain']}_THREAD_ID")),
                text=admin_message
            )
            await message.reply_text(
                'ጥቆማዎን ስላቅረቡ እናመሰግናለን ✅ጥቆማዎን በሚገባ ተመልክተን አስፈላጊ እርምጃዎችን እንወስዳለን \n\n'
                    'ጥቆማዎን በሚከተሉት ስልክ ቁጥሮች  📞 በመደወል መከታተል ይችላሉ ፡ \n\n'
                    'እሰይ ጴጥሮስ – 0926435305 \n\n'
                    'ኮማንደር ሃይሉ – 0913405901 '
            )
        elif context.user_data['language'] == 'sidama':
            await context.bot.send_message(
                chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID,
                message_thread_id=int(os.getenv(f"SIDAMA_OROMO_THEFT_THREAD_ID")),
                text=admin_message
            )
            await message.reply_text(
               'Waan ripoortii gootaniif guddaa galatooma. ✅ Ripoortiin keessan erga ilaalame booda gochi seera qabeessa ta\'ee ni fudhatama\n'
                    'Adeemsa qorannoo kana duukaa bu\'uuf lakkofsota kana fayyadamu ni dandeessu:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu  0913405901 '
            )
        elif context.user_data['language'] == 'oromia':
            await context.bot.send_message(
                chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID,
                message_thread_id=int(os.getenv('SIDAMA_OROMO_THEFT_THREAD_ID')),
                text=admin_message
            )
            await message.reply_text(
                'Waan ripoortii gootaniif guddaa galatooma. ✅ Ripoortiin keessan erga ilaalame booda gochi seera qabeessa ta\'ee ni fudhatama\n'
                    'Adeemsa qorannoo kana duukaa bu\'uuf lakkofsota kana fayyadamu ni dandeessu:\n\n'
                    'Essay Petros – 0926435305\n\n'
                    'Commander Hailu – 0913405901 ' 
            )
        else:
            await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

        keys_to_remove = ('theft_owner', 'theft_name', 'theft_item', 'theft_date&time', 'reported_theft', 'theft_location')
        for key in keys_to_remove:
            context.user_data.pop(key, None)

async def reporting_theft(update: Update, context: ContextTypes.DEFAULT_TYPE, owner: str, step: int):
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message

    context.user_data['theft_owner'] = owner
    context.user_data['message_step'] = step

    if owner == 'own':
        if step == 1:
            english_reported_button = [
                [InlineKeyboardButton('Yes', callback_data='report_yes')],
                [InlineKeyboardButton('No', callback_data='report_no')]
            ]
            amharic_reported_button = [
                [InlineKeyboardButton('አመልክቻለሁ', callback_data='report_yes')],
                [InlineKeyboardButton('አላመለከትኩም', callback_data='report_no')]
            ]
            oromia_reported_button = [
                [InlineKeyboardButton('Eyyee', callback_data='report_yes')],
                [InlineKeyboardButton('Lakki', callback_data='report_no')]
            ]
            sidama_reported_button = [
                [InlineKeyboardButton('Ee', callback_data='report_yes')],
                [InlineKeyboardButton('Dee ni', callback_data='report_no')]
            ]

            if context.user_data['language'] == 'english':
                reply_markup = InlineKeyboardMarkup(english_reported_button)
                await message.reply_text('Did you report the incident to the police?', reply_markup=reply_markup)
            elif context.user_data['language'] == 'amharic':
                reply_markup = InlineKeyboardMarkup(amharic_reported_button)
                await message.reply_text('የንብረት ስርቆቱን ለፖሊስ አመልክተዋል.?', reply_markup=reply_markup)
            elif context.user_data['language'] == 'sidama':
                reply_markup = InlineKeyboardMarkup(sidama_reported_button)
                await message.reply_text('Moorami yannara polisete kulitto/a?', reply_markup=reply_markup)
            elif context.user_data['language'] == 'oromia':
                reply_markup = InlineKeyboardMarkup(oromia_reported_button)
                await message.reply_text('Gocha kana pooliisitti riportii gochuu ni barbaaddu?', reply_markup=reply_markup)
            else:
                await message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

        elif step == 2:
            await detail_theft(update, context, 1, owner)

    elif owner == 'others':
        await detail_theft(update, context, 1, owner)