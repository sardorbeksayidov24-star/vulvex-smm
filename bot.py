import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import Command

# --- SOZLAMALAR ---
BOT_TOKEN = "8835809644:AAFapOaMC8SXgxISGTq7Jz9huCmLYLO7oAU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
user_balances = {}

# --- ASOSIY MENYU ---
@dp.message(Command("start"))
@dp.message(F.text == "⬅️ Bosh menyuga")
async def start_command(message: types.Message):
    main_builder = ReplyKeyboardBuilder()
    main_builder.add(KeyboardButton(text="🎟️ Danat qilish"), KeyboardButton(text="🗂️ Xizmatlar"))
    main_builder.add(KeyboardButton(text="💳 Pul kiritish"), KeyboardButton(text="💳 Hisobim"))
    main_builder.add(KeyboardButton(text="👥 Referal"), KeyboardButton(text="📊 Buyurtmalarim"))
    main_builder.add(KeyboardButton(text="📕 Qo'llanma"), KeyboardButton(text="☎️ Qo'llab-quvvatlash"))
    main_builder.add(KeyboardButton(text="🤝 Hamkorlik dasturi"))
    main_builder.adjust(2, 2, 2, 2, 1)
    await message.answer(f"Salom {message.from_user.full_name}! Xush kelibsiz.", reply_markup=main_builder.as_markup(resize_keyboard=True))

# --- XIZMATLAR ---
@dp.message(F.text == "🗂️ Xizmatlar")
async def services_command(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(KeyboardButton(text="🛍️ Telegram"), KeyboardButton(text="🛍️ Instagram"))
    kb.add(KeyboardButton(text="⬅️ Bosh menyuga"))
    await message.answer("Xizmatni tanlang:", reply_markup=kb.as_markup(resize_keyboard=True))

@dp.message(F.text == "🛍️ Instagram")
async def instagram_services(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="👤 Obunachilar", callback_data="ig_subs"))
    builder.row(InlineKeyboardButton(text="❤️ Like", callback_data="ig_likes"))
    builder.row(InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu"))
    await message.answer("Instagram xizmatlari:", reply_markup=builder.as_markup())

# --- ASOSIY FUNKSIYALAR ---
@dp.message(F.text == "💳 Hisobim")
async def show_balance(message: types.Message):
    await message.answer(f"Sizning balansingiz: {user_balances.get(message.from_user.id, 0)} so'm")

# --- BOTNI ISHGA TUSHIRISH ---
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
