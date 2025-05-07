from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import mainMenu, handleTheftComplaint as theftHandle

async def button_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.callback_query:
        query = update.callback_query
        await query.answer()
        data = query.data

    # IF THE BUTTON CLICKED WAS FROM THE LANGUAGE MENU
    if data.startswith('lang_'):
        language = data.split('_')[1]
        context.user_data['language'] = language
        await query.message.reply_text(f"✅ Language set to {language.capitalize()}")
        await mainMenu.show_main_menu(update.callback_query, context)

    elif data.startswith('location_'):
        theft_location= data.split('_')[1]
        context.user_data['theft_location']=theft_location
        await theftHandle.detail_theft(update,context,4,context.user_data['theft_owner'])

    # THE OPTIONS FOR WHOSE THE STOLEN PROPERTY IS
    elif data.endswith('_theft'):
        item=data.split('_')[0]

        #IF THE PROPERTY IS THEIRS
        if item=='own':
           await theftHandle.reporting_theft(update,context,item,1)

        #IF THE PROPERTY IS SOMEONE ELSES
        elif item=='others':
            await theftHandle.reporting_theft(update,context,item,step=1)

    elif data.startswith('report_'):
        reported=data.split('_')[1]
        context.user_data['reported_theft']=reported
        await theftHandle.reporting_theft(update,context,'own',step=2)

    #IF THE BUTTON CLICKED WAS FROM THE COMPLAINT MENU
    elif data.endswith('_issue') :
        complain=data.split('_')[0]

        #STORES WHAT THE USER CHOSE FROM THE COMPLAIN MENU TO THEIR SESSION
        context.user_data['complain']=complain

        #IF THE USER CHOSE THE THEFT OPTION
        if complain=='theft':
            english_theft_option_button=[
                [InlineKeyboardButton('🧍‍♂️ My own property',callback_data='own_theft')],
                [InlineKeyboardButton('👥 Someone else\'s property',callback_data='others_theft')]
            ]
            amharic_theft_option_button=[
                [InlineKeyboardButton('🧍‍♂️ የራሴ ንብረት',callback_data='own_theft')],
                [InlineKeyboardButton('👥 የሌላ ሰው ንብረት',callback_data='others_theft')]
            ]
            oromia_theft_option_button=[
                [InlineKeyboardButton('🧍‍♂️ Qabeenya koo',callback_data='own_theft')],
                [InlineKeyboardButton('👥 Qabeenya nama ambiraa',callback_data='others_theft')]
            ]
            sidama_theft_option_button=[
                [InlineKeyboardButton('🧍‍♂️ Ane jajjaati/uduunnichooti',callback_data='own_theft')],
                [InlineKeyboardButton('👥  Wolu manni jajjaati/uduunnichooti ',callback_data='others_theft')]
            ]


            if context.user_data['language']=='english':
                reply_markup=InlineKeyboardMarkup(english_theft_option_button)
                await query.message.reply_text('Was the stolen property your own or someone else\'s?', reply_markup=reply_markup)

            elif context.user_data['language']=='amharic':
                reply_markup=InlineKeyboardMarkup(amharic_theft_option_button)
                await query.message.reply_text('የተሰረቀው የማን ንብረት ነው \n የራስዎ ወይስ የሌላ ሰው? ', reply_markup=reply_markup)
                
            elif context.user_data['language']=='sidama':
                reply_markup=InlineKeyboardMarkup(sidama_theft_option_button)
                await query.message.reply_text(' Mooramino jajji/uduunni atehonso wolu manniho?', reply_markup=reply_markup)

            elif context.user_data['language']=='oromia':
                reply_markup=InlineKeyboardMarkup(oromia_theft_option_button)
                await query.message.reply_text('Qabeenyi hatame kan keessani moo kan nama ambiraati?', reply_markup=reply_markup)

            else:
                await query.message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")
                
    #IF THE USER CHOSE A COMPLAINT OTHER THAN THEFT                
        else:
            if context.user_data['language']=='english':
                await query.message.reply_text(f"Great! Please type your {complain} complain below ✍️")
            elif context.user_data['language']=='amharic':
                await query.message.reply_text(f"እባክዎ ቅሬታዎን ይጻፉልን ✍️")
            elif context.user_data['language']=='sidama':
                await query.message.reply_text(f"Lowonta danchaho! Hee'rannohe koffeenya konni woroonni borreessi ✍️")
            elif context.user_data['language']=='oromia':
                await query.message.reply_text(f"Gaarii, maaloo komii nuuf barreessaa ✍️")
            else:
                await query.message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

    # IF THE USER CHOSE SUGGESTION FROM THE MAIN MENU             
    elif data=='suggestion' :
        context.user_data['choice'] = data
        if context.user_data['language']=='english':
            await query.message.reply_text(f"Great! Please type your suggestion below ✍️")
        elif context.user_data['language']=='amharic':
            await query.message.reply_text(f"እባክዎ ሃሳብ /አስተያየትዎን ይጻፉልን✍️")
        elif context.user_data['language']=='sidama':
            await query.message.reply_text(f"Lowonta danchaho! Hedokki konni woroonni xawisi ✍️")
        elif context.user_data['language']=='oromia':
            await query.message.reply_text(f"Gaarii, maaloo yaada/ilaalcha nuuf barreessaa ✍️")
        else:
            await query.message.reply_text("Sorry something went wrong. Please restart the bot by using the /start command.")

    # IF THE USER CHOSE SUGGESTION FROM THE MAIN MENU
    elif data=='complaint':    

        #STORES WHAT THE USER CLICKED FROM THE MAIN MENU TO THEIR SESSION
        context.user_data['choice'] = data

        english_complain_button=[
            
               [ InlineKeyboardButton('Cafe 🍽️', callback_data='cafe_issue'),
                InlineKeyboardButton('Dorm 🏠', callback_data='dorm_issue'),
                InlineKeyboardButton('Academic 📚', callback_data='academic_issue')
                ],
                [InlineKeyboardButton('Cleaning 🧹', callback_data='cleaning_issue'),
                InlineKeyboardButton('Repair & Maintenance 🔧', callback_data='repair_issue'),
                InlineKeyboardButton('Clinic 🏥', callback_data='clinic_issue')
                ],

                [InlineKeyboardButton('Reporting Theft 🚨', callback_data='theft_issue')]
            
        ]
        amharic_complain_button=[
            
               [ InlineKeyboardButton('የካፌ አገልግሎት 🍽️', callback_data='cafe_issue'),
                InlineKeyboardButton('የዶርሚተሪ አገልግሎት 🏠', callback_data='dorm_issue'),
                InlineKeyboardButton('የአካዳሚክ ጉዳይ 📚', callback_data='academic_issue')
                ],
                [InlineKeyboardButton('የፅዳት ጉዳዮች 🧹', callback_data='cleaning_issue'),
                InlineKeyboardButton('የጥገና ጥቆማ 🔧', callback_data='repair_issue'),
                InlineKeyboardButton('የክሊኒክ አገልግሎት 🏥', callback_data='clinic_issue')
                ],

                [InlineKeyboardButton('የንብረት ስርቆት ጥቆማ 🚨', callback_data='theft_issue')]
            
        ]
        sidama_complain_button=[
            
               [ InlineKeyboardButton('Sagalete base/kaaffe lainohunni 🍽️', callback_data='cafe_issue'),
                InlineKeyboardButton('Gallanniwa/Dormete owaataano aana 🏠', callback_data='dorm_issue'),
                InlineKeyboardButton('Rosanna rosiisa lainohunni 📚', callback_data='academic_issue')
                ],
                [InlineKeyboardButton('Qarqaru co\'imma hajo  lainohunni 🧹', callback_data='cleaning_issue'),
                InlineKeyboardButton('Gatamarshu owaante lainohunni 🔧', callback_data='repair_issue'),
                InlineKeyboardButton('Fayyimmate owaante lainohunni 🏥', callback_data='clinic_issue')
                ],

                [InlineKeyboardButton('Jajju bairo eersate 🚨', callback_data='theft_issue')]
            
        ]
        oromia_complain_button=[
            
               [ InlineKeyboardButton('Komii kaaffee 🍽️', callback_data='cafe_issue'),
                InlineKeyboardButton('Komii doormii 🏠', callback_data='dorm_issue'),
                InlineKeyboardButton('Komii akkaadami 📚', callback_data='academic_issue')
                ],
                [InlineKeyboardButton('Komii qulqullinaa 🧹', callback_data='cleaning_issue'),
                InlineKeyboardButton('Komii suuphaa fi caccabuu 🔧', callback_data='repair_issue'),
                InlineKeyboardButton('Komii kilinikii 🏥', callback_data='clinic_issue')
                ],

                [InlineKeyboardButton('Komii hattummaa 🚨', callback_data='theft_issue')]
            
        ]

        if context.user_data['language']=='english':
            reply_markup= InlineKeyboardMarkup(english_complain_button)
            await query.message.reply_text("Please select a category for your complaint: 📝", reply_markup=reply_markup)
        elif context.user_data['language']=='amharic':
            reply_markup= InlineKeyboardMarkup(amharic_complain_button)
            await query.message.reply_text("እባኮትን የቅሬታዎን ምድብ ይምረጡ: 📝", reply_markup=reply_markup)
        elif context.user_data['language']=='sidama':
            reply_markup= InlineKeyboardMarkup(sidama_complain_button)
            await query.message.reply_text("Hee'rannohe koffeenya booso boosontenni doori: 📝", reply_markup=reply_markup)
        elif context.user_data['language']=='oromia':
            reply_markup= InlineKeyboardMarkup(oromia_complain_button)
            await query.message.reply_text("Maaloo kutaa komii keessani filadhaa: 📝", reply_markup=reply_markup)
        else:
            await query.message.reply_text("Sorry something went wrong. Please restart the bot using the /start command")

        
    else:
        await query. message.reply_text("Something went wrong! Please restart the bot using the /start command")