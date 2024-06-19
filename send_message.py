import asyncio
import telegram
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder

API_TOKEN = '7462674994:AAGv1gLMqoxQ4Z7_ZpROZLBR_aqxRINekoo'
CHANNEL_ID = '-1002240815695'

reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("X(Twitter)", callback_data="https://x.com/moonmouse24", url="https://x.com/moonmouse24"),
            InlineKeyboardButton("Website", callback_data="https://moonmouse.io", url="https://moonmouse.io"),
        ],
        [InlineKeyboardButton("Tap to Verify", callback_data="http://t.me/safeguard?start=-1002212462327", url="http://t.me/safeguard?start=-1002212462327")],
    ])

msg = "MOONMOUSE (Chat) $MMOUSE is being protected by \n @Safeguard \n\n Click below to verify you're human"
video_url='MoonMouse.mp4'

# using telegram.Bot
async def send(chat, video, message, reply_markup):
    await Bot(API_TOKEN).send_video(chat_id=chat, video=video, caption=message, reply_markup=reply_markup)

asyncio.run(send(CHANNEL_ID, video_url, msg, reply_markup))
