from telethon import TelegramClient, events
import urllib.parse
from telethon.tl.types import InputWebDocument
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (if available)
load_dotenv()



api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
bot_token = os.getenv("BOT_TOKEN", '')

bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Handle the /start command
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hi! just send something you're curious about")

@bot.on(events.InlineQuery())
async def inline(event):
    builder = event.builder

    message = event.text
    if not message:
        return
    google_logo_url = "https://1000logos.net/wp-content/uploads/2016/11/New-Google-Logo.jpg"
    gpt_logo_url = "https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png"

    google_thumb = InputWebDocument(
        url=google_logo_url,
        size=0,  
        mime_type='image/png',  
        attributes=[]  
    )
    gpt_thumb = InputWebDocument(
        url=gpt_logo_url,
        size=0,
        mime_type='image/png',
        attributes=[]
    )

    search_query = urllib.parse.quote(message)
    lmgTFY_link = f'https://letmegooglethat.com/?q={search_query}'
    lmcTFY_link = f'https://letmegpt.com/?q={search_query}'
    await event.answer([
        builder.article(
            title=f'google {message}',
            text=f'\n\n\n <a href="{lmgTFY_link}">{message}</a>',
            thumb=google_thumb,
            description='Search on Google',
            parse_mode='HTML'  
        ),
        builder.article(
            title=f'chatgpt {message}',
            text=f'\n\n\n <a href="{lmcTFY_link}">{message}</a>',
            thumb=gpt_thumb,
            description='chat with AI',
            parse_mode='HTML'  
        )
    ])

bot.run_until_disconnected()
