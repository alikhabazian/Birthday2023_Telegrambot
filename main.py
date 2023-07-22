from telegram import Update,ReplyKeyboardMarkup,constants
from telegram.ext import filters, MessageHandler,ApplicationBuilder, ContextTypes, CommandHandler,ConversationHandler,PicklePersistence
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
    # print(update.effective_message.message_id)
    
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
        message_id=126#sabr
    )

    
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[3]['question']
    )


    return SABR


async def azat(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        message_id=246#azat
    )

    
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[5]['question']
    )


    return AZAT

async def memoery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Your answer was correct'
    )
    # print(update.effective_message.chat_id)
    
    # await context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text='وقت اذیت کردنه\n باید آهنگم را سعی کنی با صدای خودت هر جور فکر میکنی قشنگه بخونی و گرنه باید چند ساعت منتظر بمونی ممکنه بقیه بیوفتن جلو '
    # )
    
    # await context.bot.forward_message(
    #     chat_id=update.effective_chat.id,
    #     from_chat_id=684630739,
    #     message_id=126#azat
    # )

    
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[7]['question']
    )


    return MEMOERY


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
        text="it is sent to me and waiting to response"
    )
    
async def dvorak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[2]['question']
    )
    return DVORAK

async def fuckyou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[4]['question']
    )
    arr_images=[
        'AgACAgQAAxkBAAOWZJ3hLJauWu12-P26O09eAh4coAkAAjC-MRtnTPFQvw5DiX-YlLwBAAMCAANzAAMvBA',
        'AgACAgQAAxkBAAOXZJ3hW2NOeCkb93dxCK2QiHg6HN8AAjK-MRtnTPFQGLQssl9OWskBAAMCAANzAAMvBA',
        'AgACAgQAAxkBAAOYZJ3hhkqHjlIdlS5zU1Rc34xMk7EAAjO-MRtnTPFQte3b6UiToZUBAAMCAANzAAMvBA'
    ]
    #first #AgACAgQAAxkBAAOWZJ3hLJauWu12-P26O09eAh4coAkAAjC-MRtnTPFQvw5DiX-YlLwBAAMCAANzAAMvBA
    #second#AgACAgQAAxkBAAOXZJ3hW2NOeCkb93dxCK2QiHg6HN8AAjK-MRtnTPFQGLQssl9OWskBAAMCAANzAAMvBA
    #third #AgACAgQAAxkBAAOYZJ3hhkqHjlIdlS5zU1Rc34xMk7EAAjO-MRtnTPFQte3b6UiToZUBAAMCAANzAAMvBA
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=arr_images[1]
    )
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=arr_images[0]
    )
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=arr_images[2]
    )
    return FUCKYOU

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[6]['question']
    )
    return PHONE

async def jadval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Levels[8]['question']
    )

    #AgACAgQAAxkBAAPJZJ4AAfwTRIxy2xiUF9XsJ9Ws61PJAAJgvjEbZ0zxUMdy0hgFOHeiAQADAgADcwADLwQ
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo='AgACAgQAAxkBAAPJZJ4AAfwTRIxy2xiUF9XsJ9Ws61PJAAJgvjEbZ0zxUMdy0hgFOHeiAQADAgADcwADLwQ'

    )
    return JADVAL


async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #CQACAgQAAxkBAAPLZJ4Ey_hk-VkYtFj-Ou2MHhl09qYAAkUEAALZnbhS1IyQF8KCUngvBA
    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio='CQACAgQAAxkBAAPLZJ4Ey_hk-VkYtFj-Ou2MHhl09qYAAkUEAALZnbhS1IyQF8KCUngvBA')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="you have finished the game"
    )
    await context.bot.send_message(
        chat_id="-1001892648701",
        text=f"{update.effective_chat.id} finish the game"
    )
    return LOOP

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

async def pr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_message)
    

if __name__ == '__main__':
    persistence = PicklePersistence(filepath="conversationbot")
    application = ApplicationBuilder().token(TOKEN).persistence(persistence).build()
    # admin_ord=MessageHandler(filters.Regex(r'^[0-9]{5,}![a-zA-Z]+$'),admin_order)
    menue_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            # MessageHandler(None, pr)
        ],
        fallbacks=[
            MessageHandler(filters.Regex(r'^[0-9]{5,}![a-zA-Z]+$'),admin_order),
            MessageHandler(None,wrong)
        ],
        states={
         KEYBOARD:[
            MessageHandler(filters.Regex(Levels[KEYBOARD]['answer']),shamim)
         ],
         SHAMIM:[
            MessageHandler(filters.VOICE,check_music),
            MessageHandler(filters.Regex(r'^shalil$'),dvorak)
         ],
         DVORAK:[
             MessageHandler(filters.Regex(Levels[DVORAK]['answer']),sabr)
         ],
         SABR:[
            MessageHandler(filters.VOICE,check_music),
            MessageHandler(filters.Regex(r'^shaskol$'),fuckyou)
         ],
         FUCKYOU:[
            MessageHandler(filters.Regex(r'fuck'),azat)
         ],
         AZAT:[#music must update
             MessageHandler(filters.VOICE,check_music),
             MessageHandler(filters.Regex(r'^shazam$'),phone)
         ],
         PHONE:[
             MessageHandler(filters.Regex(r'^salam kon sag$'),memoery)
         ],
         MEMOERY:
         [  
             MessageHandler(filters.VOICE,check_music),
             MessageHandler(filters.Regex(r'^yadeshXbeXkheir$'),jadval)
         ],
         JADVAL:[
             MessageHandler(filters.Regex(Levels[JADVAL]['answer']),finish)
         ],
         LOOP:[
             
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

        },
        persistent=True,
        name='puzzle'
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

