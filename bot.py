import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# O'zingizning ishlaydigan haqiqiy tokeningizni shu yerga qo'ying:
TOKEN = "8835809644:AAFapOaMC8SXgxISGTq7Jz9huCmLYLO7oAU"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- 1. ASOSIY MENYU (START BOSILGANDA) ---
@dp.message(CommandStart())
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    
    builder.add(types.KeyboardButton(text="🎟️ Danat qilish"))
    builder.add(types.KeyboardButton(text="📁 Xizmatlar"))
    
    builder.add(types.KeyboardButton(text="💳 Pul kiritish"))
    builder.add(types.KeyboardButton(text="💳 Hisobim"))
    
    builder.add(types.KeyboardButton(text="👥 Referal"))
    builder.add(types.KeyboardButton(text="📊 Buyurtmalarim"))
    
    builder.add(types.KeyboardButton(text="📕 Qo'llanma"))
    builder.add(types.KeyboardButton(text="☎️ Qo'llab-quvvatlash"))
    
    builder.add(types.KeyboardButton(text="🤝 Hamkorlik dasturi"))
    
    builder.adjust(2, 2, 2, 2, 1)
    
    # Bu yerda nomingiz rasman VULVEX SMM bo'ldi:
    await message.answer(
        f"Salom {message.from_user.full_name}! VULVEX SMM botiga xush kelibsiz!\nQuyidagi menyudan kerakli bo'limni tanlang:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

# --- 2. XIZMATLAR BO'LIMI ---
@dp.message(F.text == "📁 Xizmatlar")
async def xizmatlar_command(message: types.Message):
    services_builder = ReplyKeyboardBuilder()
    
    services_builder.add(types.KeyboardButton(text="🛍️ Telegram"))
    services_builder.add(types.KeyboardButton(text="🛍️ Instagram"))
    services_builder.add(types.KeyboardButton(text="🛍️ Tik Tok"))
    services_builder.add(types.KeyboardButton(text="🛍️ You tube"))
    services_builder.add(types.KeyboardButton(text="🛍️ Facebook"))
    services_builder.add(types.KeyboardButton(text="🛍️ Threads"))
    services_builder.add(types.KeyboardButton(text="⭐ Premium, Starts, Gift"))
    services_builder.add(types.KeyboardButton(text="⬅️ Ortga"))
    
    services_builder.adjust(2, 2, 2, 1, 1)
    
    await message.answer(
        "👇 Quyidagi ijtimoiy tarmoqlardan birini tanlang.",
        reply_markup=services_builder.as_markup(resize_keyboard=True)
    )

# --- 3. DONAT DO'KONI BO'LIMI ---
@dp.message(F.text == "🎟️ Danat qilish")
async def danat_command(message: types.Message):
    donat_builder = ReplyKeyboardBuilder()
    
    donat_builder.add(types.KeyboardButton(text="🎮 Pubg Uc"))
    donat_builder.add(types.KeyboardButton(text="🎮 Free Fire Almaz"))
    donat_builder.add(types.KeyboardButton(text="🎮 Mobile Legends"))
    donat_builder.add(types.KeyboardButton(text="⬅️ Ortga"))
    
    donat_builder.adjust(1, 1, 1, 1)
    
    await message.answer(
        "🎟️ Donat do'koni\n\nQuyidagi ichki bo'limlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=donat_builder.as_markup(resize_keyboard=True)
    )

# --- 4. ORTGA QAYTISH TUGMASI ---
@dp.message(F.text == "⬅️ Ortga")
async def back_command(message: types.Message):
    await start_command(message)

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__== "__main__":
    asyncio.run(main())