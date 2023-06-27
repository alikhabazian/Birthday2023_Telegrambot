from telegram import Update,ReplyKeyboardMarkup,constants
from telegram.ext import filters, MessageHandler,ApplicationBuilder, ContextTypes, CommandHandler,ConversationHandler
from datas import *

TOKEN='6183737223:AAFc8MK_2_Jrw8Oy6j360pZc-X7vxTo6puQ'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('start')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        # chat_id="-1001892648701",
        text=Levels[0]['question']
    )

    return KEYBOARD



async def shamim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Your answer was correct'
    )
    print(update.effective_message.message_id)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='وقت اذیت کردنه\n باید آهنگم را سعی کنی با صدای خودت هر جور فکر میکنی قشنگه بخونی و گرنه باید چند ساعت منتظر بمونی ممکنه بقیه بیوفتن جلو '
    )
    
    await context.bot.forward_message(
        chat_id=update.effective_chat.id,
        from_chat_id=684630739,
        message_id=31#shamim
    )

    
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[1]['question']
    )


    return SHAMIM


async def sabr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Your answer was correct'
    )
    # print(update.effective_message.chat_id)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='وقت اذیت کردنه\n باید آهنگم را سعی کنی با صدای خودت هر جور فکر میکنی قشنگه بخونی و گرنه باید چند ساعت منتظر بمونی ممکنه بقیه بیوفتن جلو '
    )
    
    await context.bot.forward_message(
        chat_id=update.effective_chat.id,
        from_chat_id=684630739,
        message_id=64#sabr
    )

    
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[3]['question']
    )


    return SABR


async def check_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(
        chat_id="-1001892648701",
        from_chat_id=update.effective_message.chat_id,
        message_id=update.effective_message.message_id,
    )

    await context.bot.send_message(
        chat_id='-1001892648701',
        text=f"{update.effective_message.chat_id}"
    )
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="it is send to me and waiting to response"
    )
    


async def dvorak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[2]['question']
    )
    return DVORAK

async def wrong(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="your answer is wrong!"
    )

async def admin_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_message.text.split('!')[0],
        text=update.effective_message.text.split('!')[1]
    )

    

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    # admin_ord=MessageHandler(filters.Regex(r'^[0-9]{5,}![a-zA-Z]+$'),admin_order)
    menue_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ,
        #MessageHandler(filters.TEXT & (~filters.COMMAND), unknown_command)
        ],
        fallbacks=[
            MessageHandler(filters.Regex(r'^[0-9]{5,}![a-zA-Z]+$'),admin_order),
            MessageHandler(None,wrong)
        ],
        states={
         KEYBOARD:[
            MessageHandler(filters.VOICE,shamim),
            MessageHandler(filters.Regex(Levels[KEYBOARD]['answer']),shamim)
                # CommandHandler('start', start),
                # MessageHandler(filters.Regex(labbels[HOME][0]),ready_to_add_channel),
                # MessageHandler(filters.Regex(labbels[HOME][1]),list_channel),
         ],
         SHAMIM:[
            MessageHandler(filters.VOICE,check_music),
            MessageHandler(filters.Regex(r'^shalil$'),dvorak)
         ],
         DVORAK:[
             MessageHandler(filters.Regex(Levels[DVORAK]['answer']),sabr)
         ]
        #  INSERTING_CHANNEL:[
        #         CommandHandler('start', start),
        #         MessageHandler(filters.TEXT,add_channel),
        #  ],
        #  SELECTING_CHANNEL:[
        #         CommandHandler('start', start),
        #         MessageHandler(filters.TEXT,collect_channel),
        #  ],
        #  SENDING_IMAGE:[
        #         CommandHandler('start', start),
        #         MessageHandler(filters.Document.ALL,income_file),
        #  ]
        }
    )
    application.add_handler(menue_handler)
    # application.add_handler(admin_ord)
    # print(dotenv_values(os.path.join(dir_path, ".env"))['PORT'])
    # application.run_webhook(
    # listen='0.0.0.0',
    # port = dotenv_values(os.path.join(dir_path, ".env"))['PORT'],
    # secret_token=secrets.token_urlsafe(16),
    # key='private.key',
    # cert='cert.pem',
    # webhook_url='https://{}:{}'.format(dotenv_values(os.path.join(dir_path, ".env"))['DOMAIN'], dotenv_values(os.path.join(dir_path, ".env"))['PORT'])
    # )

    application.run_polling()

