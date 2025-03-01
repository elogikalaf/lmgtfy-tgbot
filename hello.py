from telethon import TelegramClient, events
import urllib.parse
from telethon.tl.types import InputWebDocument
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (if available)
load_dotenv()

api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
# Load bot token from .env file
bot_token = os.getenv("BOT_TOKEN", '')

# start the bot
bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Handle the /start command
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hi! just send something you're curious about")

# Handle inline queries
@bot.on(events.InlineQuery())
async def inline(event):
    builder = event.builder
    message = event.text

    # Put exception if there's no inline message, not putting this here gives an error while building the query url
    if not message:
        return

    google_logo_url = "https://1000logos.net/wp-content/uploads/2016/11/New-Google-Logo.jpg"
    gpt_logo_url = "https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png"

    # Set the thumbnail using the InputWebDocument interface 
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

    # Set the links using the input inline message
    search_query = urllib.parse.quote(message)
    lmgTFY_link = f'https://letmegooglethat.com/?q={search_query}'
    lmcTFY_link = f'https://letmegpt.com/?q={search_query}'

    # Build inline results 
    await event.answer([
        builder.article(
            title=f'google {message}',
            # Create an hyperlink using the HTML parse mode
            text=f'\n\n\n <a href="{lmgTFY_link}">{message}</a>',
            thumb=google_thumb,
            description='Search on Google',
            parse_mode='HTML'  
        ),
        builder.article(
            title=f'chatgpt {message}',
            # Create an hyperlink using the HTML parse mode
            text=f'\n\n\n <a href="{lmcTFY_link}">{message}</a>',
            thumb=gpt_thumb,
            description='chat with AI',
            parse_mode='HTML'  
        )
    ])

bot.run_until_disconnected()
