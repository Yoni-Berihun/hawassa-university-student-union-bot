from telegram import Update
from telegram.ext import ContextTypes
import handleTheftComplaint as theftHandle

from dotenv import load_dotenv
import os,re
load_dotenv()

ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))
SIDAMA_OROMO_ADMIN_CHAT_ID= int(os.getenv('SIDAMA_OROMO_ADMIN_CHAT_ID'))

def contains_link(text: str) -> bool:
    # Basic pattern to detect links
    pattern = r"(https?://\S+)|(\w+\.(com|net|org|gov|edu|info|io|me|co))"
    return re.search(pattern, text) is not None


async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # PREVENTS GROUPS FROM REPLYING TO THE BOT
    if update.effective_chat.type in ['group', 'supergroup']:
        return
    
    user_text = update.message.text
    if contains_link(user_text):
        await update.message.reply_text("❌ Links are not allowed. Please enter only valid text without links.")
        return

    choice = context.user_data.get('choice')
    complain = context.user_data.get('complain')

    #IF THE USER JUST SENDS A MESSAGE WITHOUT CHOOSING AN OPTION 
    if not choice:
        await update.message.reply_text("Please start with /start and select an option...")
        return
    
    context.user_data['user'] = update.effective_user.username
     
    if complain=='theft':
        step=context.user_data['message_step']
        
        if step==1:
            context.user_data['theft_item']=user_text
            await theftHandle.detail_theft(update,context,2,context.user_data['theft_owner'])

        elif step==2:
            context.user_data['theft_name']=user_text
            await theftHandle.detail_theft(update,context,3,context.user_data['theft_owner'])

        elif step==4:
            theft_location=context.user_data['theft_location']

            if theft_location=='dorm':
                context.user_data['theft_block&dorm']=user_text
                await theftHandle.detail_theft(update,context,5,context.user_data['theft_owner'])

            elif theft_location=='library':
                context.user_data['theft_date&time']=user_text
                await theftHandle.detail_theft(update,context,5,context.user_data['theft_owner'])

            elif theft_location=='other':
                context.user_data['theft_other_loc']=user_text
                await theftHandle.detail_theft(update,context,5,context.user_data['theft_owner'])

        elif step==5:
            theft_location=context.user_data['theft_location']

            context.user_data['theft_date&time']=user_text
            await theftHandle.detail_theft(update,context,6,context.user_data['theft_owner'])           
    
    else:

        if context.user_data['language']=='english':
            await update.message.reply_text(f"✅ Thank you for your {choice}! We'll look into it!")
            if complain:
                admin_message = f"New {choice} about {complain}:\n\n{user_text}"
                await context.bot.send_message(chat_id=ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'{complain.upper()}_THREAD_ID')), text=admin_message)
            elif choice=='suggestion':
                admin_message = f"New {choice}:\n\n{user_text}"
                await context.bot.send_message(chat_id=ADMIN_CHAT_ID, message_thread_id= int(os.getenv('SUGGESTIONS_THREAD_ID')), text=admin_message)


        elif context.user_data['language']=='sidama':
            await update.message.reply_text(f"✅ Shiqishootto/a koffeenyi daafira galateemmo. Qoleno la'neemmona ikkanno!")
            if complain:
                admin_message = f"New {choice} about {complain}:\n\n{user_text}"
                await context.bot.send_message(chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'SIDAMA_OROMO_{complain.upper()}_THREAD_ID')) , text=admin_message)
            elif choice=='suggestion':
                admin_message = f"New {choice}:\n\n{user_text}"
                await context.bot.send_message(chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'SIDAMA_OROMO_SUGGESTIONS_THREAD_ID')),  text=admin_message)


        elif context.user_data['language']=='oromia':
            await update.message.reply_text(f"✅ {'Komii' if choice=='complaint' else 'ilaalcha'} keessanif  galatoomaa! ni ilaalla!")
            if complain:
                admin_message = f"New {choice} about {complain}:\n\n{user_text}"
                await context.bot.send_message(chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'SIDAMA_OROMO_{complain.upper()}_THREAD_ID')), text=admin_message)
            elif choice=='suggestion':
                admin_message = f"New {choice}:\n\n{user_text}"
                await context.bot.send_message(chat_id=SIDAMA_OROMO_ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'SIDAMA_OROMO_SUGGESTIONS_THREAD_ID')), text=admin_message)


        elif context.user_data['language']=='amharic':
            await update.message.reply_text(f"✅ {'ለቅሬታዎ' if choice=='complaint' else 'ለአስተያየትዎ'} እጅግ እናመሰግናለን! እንደሚገባው እንመርመራለን!")
            if complain:
                admin_message = f"New {choice} about {complain}:\n\n{user_text}"
                await context.bot.send_message(chat_id=ADMIN_CHAT_ID, message_thread_id= int(os.getenv(f'{complain.upper()}_THREAD_ID')), text=admin_message)
            elif choice=='suggestion':
                admin_message = f"New {choice}:\n\n{user_text}"
                await context.bot.send_message(chat_id=ADMIN_CHAT_ID, message_thread_id= int(os.getenv('SUGGESTIONS_THREAD_ID')), text=admin_message)


        else:
            await update.message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")