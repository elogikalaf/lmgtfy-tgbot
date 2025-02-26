from telethon import TelegramClient, events, Button
import urllib.parse

from telethon.tl.types import InputWebDocument



api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
bot_token = '*'

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

    # Create InputWebDocument objects for the thumbnails
    google_thumb = InputWebDocument(
        url=google_logo_url,
        size=0,  # Size is optional, set to 0 if unknown
        mime_type='image/png',  # MIME type of the image
        attributes=[]  # Additional attributes (optional)
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
            # text=f'*there you go, was it that hard?* \n\n\n [{message}]({lmgTFY_link})',
            text=f'\n\n\n <a href="{lmgTFY_link}">{message}</a>',
            thumb=google_thumb,
            description='Search on Google',
            # link_preview=False,  # Note: Correct spelling is `link_preview`, not `link_preview`
            parse_mode='HTML'  # Uncommented and set to 'Markdown'
        ),
        builder.article(
            title=f'chatgpt {message}',
            text=f'\n\n\n <a href="{lmcTFY_link}">{message}</a>',
            thumb=gpt_thumb,
            description='chat with AI',
            # link_preview=False,  # Note: Correct spelling is `link_preview`, not `link_preview`
            parse_mode='HTML'  # Uncommented and set to 'Markdown'
        )
    ])

# Run the bot
bot.run_until_disconnected()
