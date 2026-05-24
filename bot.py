import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --- 1. SOZLAMALAR ---
# BotFather'dan olgan tokeningizni shu yerga yozing
BOT_TOKEN = "8835809644:AAFapOaMC8SXgxISGTq7Jz9huCmLYLO7oAU"
# O'zingizning Telegram ID raqamingizni shu yerga yozing (Adminga murojaat uchun)
ADMIN_ID = 6831436355  

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- 2. ASOSIY MENYU (/start) ---
@dp.message(F.text == "/start")
async def start_command(message: types.Message):
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.add(KeyboardButton(text="🎁 Donat do'koni"))
    menu_builder.adjust(1)
    
    await message.answer(
        f"Salom {message.from_user.full_name}! Botimizga xush kelibsiz.",
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )

# --- 3. DONAT DO'KONI (ICHKI MENYU) ---
@dp.message(F.text == "🎁 Donat do'koni")
async def danat_command(message: types.Message):
    donat_builder = ReplyKeyboardBuilder()
    donat_builder.add(KeyboardButton(text="💳 Pul kiritish"))
    donat_builder.add(KeyboardButton(text="💰 Hisobim"))
    donat_builder.add(KeyboardButton(text="⬅️ Ortga"))
    donat_builder.adjust(1, 1, 1)  # Tugmalar bittadan qatorda Neo SMM dek chiqadi
    
    await message.answer(
        "🎁 *Donat do'koni*\n\nQuyidagi ichki bo'limlardan birini tanlang:",
        reply_markup=donat_builder.as_markup(resize_keyboard=True),
        parse_mode="Markdown"
    )

# --- 4. HISOBIM TUGMASI ---
@dp.message(F.text == "💰 Hisobim")
async def show_balance(message: types.Message):
    client_id = message.from_user.id
    await message.answer(
        f"👤 *Shaxsiy kabinet:*\n\n"
        f"🆔 *Sizning ID raqamingiz:* {client_id}\n"
        f"💰 *Sizning balansingiz:* 0 so'm\n\n"
        f"🚀 _Hisobni to'ldirish uchun '💳 Pul kiritish' tugmasidan foydalaning._",
        parse_mode="Markdown"
    )

# --- 5. NEO SMM USLUBIDAGI PUL KIRITISH OYNASI ---
@dp.message(F.text == "💳 Pul kiritish")
async def start_payment(message: types.Message):
    client_id = message.from_user.id
    
    # Xuddi Neo SMM botidagidek tagma-tag turadigan tugmalarni yasaymiz
    pay_buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔸 Payme [ Avto ]", url="https://payme.uz")],
        [InlineKeyboardButton(text="🔹 Click [ Avto ]", url="https://click.uz")],
        [InlineKeyboardButton(text="🍇 Uzum [ Avto ] +2% bonus", url="https://uzumbank.uz")],
        [InlineKeyboardButton(text="🟢 Paynet [ avto ]", url="https://paynet.uz")],
        [InlineKeyboardButton(text="🔵 Oson [ Avto ]", url="https://oson.uz")],
        [InlineKeyboardButton(text="💳 Uzcard / Humo ( karta ) +2% bonus", url="https://payme.uz")],
        [InlineKeyboardButton(text="☎️ Adminga murojaat", url=f"tg://user?id={ADMIN_ID}")]
    ])
    
    # Neo SMM botidagi matn ko'rinishi
    text = (
        "🔸 Payme, 🔹 Click, 🍇 Uzum, 🟢 Paynet,\n"
        "🔵 Oson, 🟡 Alif - ilovalariga kiring To'lov\n"
        "bo'limidan *Vulvex SMM* deb qidiring va botdagi\n"
        "ID raqamingizni kiritib to'lov qilish tugmasini\n"
        "bosing.\n\n"
        f"👤 *ID raqam:* {client_id}"
    )
    
    await message.answer(text, reply_markup=pay_buttons, parse_mode="Markdown")

# --- ORTGA QAYTISH ---
@dp.message(F.text == "⬅️ Ortga")
async def back_command(message: types.Message):
    await start_command(message)

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())