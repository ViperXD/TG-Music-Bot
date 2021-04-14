from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

✣ I am Music Player,
✣ I Can Stream Music In Voice Chats Newely Introduced By Telegram...

Use The Buttons Below To Know More About Me..**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/ImJanindu/GroupMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/InfinityBOTs_Support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Infinity_BOTs"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📣 Channel", url="https://t.me/NeonBotz")
                ]
            ]
        )
   )


