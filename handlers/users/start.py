from aiogram import types
from loader import dp, bot
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import ChatNotFound

CHANNEL_USERNAME = "@N1TDMUZB"  # Kanal username

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id

    try:
        # Foydalanuvchini kanalga a'zo bo‘lganligini tekshirish
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ["left", "kicked"]:
            raise ChatNotFound()
    except:
        # Obuna bo‘lmaganlar uchun tugmalar
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("🔔 Obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}"),
            InlineKeyboardButton("✅ Tekshirish", callback_data="check_sub")
        )
        await message.answer("👋 Botdan foydalanish uchun kanalimizga obuna bo'ling!", reply_markup=keyboard)
        return

    # Obuna bo‘lganlar uchun menyu
    await message.answer(
        "👇 Iltimos, kerakli tugmani tanlang:",
        reply_markup=types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [
                    types.KeyboardButton(
                        text="Open App",
                        web_app=WebAppInfo(url="https://instagram-free.up.railway.app/")
                    )
                ]
            ]
        )
    )

@dp.callback_query_handler(text="check_sub")
async def check_subscription(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ["left", "kicked"]:
            raise ChatNotFound()
    except:
        await callback.answer("🚫 Hali obuna bo‘lmagansiz!", show_alert=True)
        return

    await callback.message.delete()
    await callback.message.answer(
        "👇 Iltimos, kerakli tugmani tanlang:",
        reply_markup=types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [
                    types.KeyboardButton(
                        text="Open App",
                        web_app=WebAppInfo(url="https://instagram-free.up.railway.app/")
                    )
                ]
            ]
        )
    )
