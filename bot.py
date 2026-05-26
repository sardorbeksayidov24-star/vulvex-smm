import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
# --- 1. SOZLAMALAR ---
BOT_TOKEN = "8835809644:AAFapOaMC8SXgxISGTq7Jz9huCmLYLO7oAU"
ADMIN_ID = 6831436355

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_balances = {}
# --- 2. ASOSIY MENYU ---
@dp.message(F.text == "/start")
@dp.message(F.text == "⬅️ Bosh menyuga")
async def start_command(message: types.Message):
    main_builder = ReplyKeyboardBuilder()
    
    main_builder.add(KeyboardButton(text="🎟️ Danat qilish"))
    main_builder.add(KeyboardButton(text="🗂️ Xizmatlar"))
    main_builder.add(KeyboardButton(text="💳 Pul kiritish"))
    main_builder.add(KeyboardButton(text="💳 Hisobim"))
    main_builder.add(KeyboardButton(text="👥 Referal"))
    main_builder.add(KeyboardButton(text="📊 Buyurtmalarim"))
    main_builder.add(KeyboardButton(text="📕 Qo'llanma"))
    main_builder.add(KeyboardButton(text="☎️ Qo'llab-quvvatlash"))
    main_builder.add(KeyboardButton(text="🤝 Hamkorlik dasturi"))
    
    main_builder.adjust(2, 2, 2, 2, 1)
    
    await message.answer(
        f"Salom {message.from_user.full_name}! Botimizga xush kelibsiz.\nQuyidagi menyudan kerakli bo'limni tanlang:",
        reply_markup=main_builder.as_markup(resize_keyboard=True)
    )
    # --- 2. ASOSIY MENYU ---
@dp.message(F.text == "/start")
@dp.message(F.text == "⬅️ Bosh menyuga")
async def start_command(message: types.Message):
    main_builder = ReplyKeyboardBuilder()
    
    main_builder.add(KeyboardButton(text="🎟️ Danat qilish"))
    main_builder.add(KeyboardButton(text="🗂️ Xizmatlar"))
    main_builder.add(KeyboardButton(text="💳 Pul kiritish"))
    main_builder.add(KeyboardButton(text="💳 Hisobim"))
    main_builder.add(KeyboardButton(text="👥 Referal"))
    main_builder.add(KeyboardButton(text="📊 Buyurtmalarim"))
    main_builder.add(KeyboardButton(text="📕 Qo'llanma"))
    main_builder.add(KeyboardButton(text="☎️ Qo'llab-quvvatlash"))
    main_builder.add(KeyboardButton(text="🤝 Hamkorlik dasturi"))
    
    main_builder.adjust(2, 2, 2, 2, 1)
    
    await message.answer(
        f"Salom {message.from_user.full_name}! Botimizga xush kelibsiz.\nQuyidagi menyudan kerakli bo'limni tanlang:",
        reply_markup=main_builder.as_markup(resize_keyboard=True)
    )
    # --- 3. XIZMATLAR BO'LIMI ---
@dp.message(F.text == "🗂️ Xizmatlar")
async def services_command(message: types.Message):
    services_builder = ReplyKeyboardBuilder()
    
    services_builder.add(KeyboardButton(text="🛍️ Telegram"))
    services_builder.add(KeyboardButton(text="🛍️ Instagram"))
    services_builder.add(KeyboardButton(text="🛍️ Tik Tok"))
    services_builder.add(KeyboardButton(text="🛍️ You tube"))
    services_builder.add(KeyboardButton(text="🛍️ Facebook"))
    services_builder.add(KeyboardButton(text="🛍️ Threads"))
    services_builder.add(KeyboardButton(text="⭐ Premium, Starts, Gift"))
    services_builder.add(KeyboardButton(text="⬅️ Bosh menyuga"))
    
    services_builder.adjust(2, 2, 2, 1, 1)
    
    await message.answer(
        "👇 Quyidagi ijtimoiy tarmoqlardan birini tanlang.",
        reply_markup=services_builder.as_markup(resize_keyboard=True)
    )

# --- 4. DANAT QILISH BO'LIMI ---
@dp.message(F.text == "🎟️ Danat qilish")
async def donat_shop_command(message: types.Message):
    donat_builder = ReplyKeyboardBuilder()
    
    donat_builder.add(KeyboardButton(text="🎮 Pubg Uc"))
    donat_builder.add(KeyboardButton(text="🎮 Free Fire Almaz"))
    donat_builder.add(KeyboardButton(text="🎮 Mobile Legends"))
    donat_builder.add(KeyboardButton(text="⬅️ Bosh menyuga"))
    
    donat_builder.adjust(1, 1, 1, 1)
    
    await message.answer(
        "🎟️ Donat do'koni\n\nQuyidagi ichki bo'limlardan birini tanlang:",
        reply_markup=donat_builder.as_markup(resize_keyboard=True)
    )
    # --- 5. HISOBIM TUGMASI ---
@dp.message(F.text == "💳 Hisobim")
async def show_balance(message: types.Message):
    client_id = message.from_user.id
    balance = user_balances.get(client_id, 0)
    await message.answer(
        f"👤 *Shaxsiy kabinet:*\n\n"
        f"🆔 *Sizning ID raqamingiz:* {client_id}\n"
        f"💰 *Sizning balansingiz:* {balance:,} so'm\n\n"
        f"🚀 _Hisobni to'ldirish uchun '💳 Pul kiritish' tugmasidan foydalaning._",
        parse_mode="Markdown"
    )

# --- 6. PUL KIRITISH ---
@dp.message(F.text == "💳 Pul kiritish")
async def start_payment(message: types.Message):
    client_id = message.from_user.id
    
    pay_buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔸 Payme [ Avto ]", url="https://payme.uz")],
        [InlineKeyboardButton(text="🔹 Click [ Avto ]", url="https://click.uz")],
        [InlineKeyboardButton(text="🍇 Uzum [ Avto ] +2% bonus", url="https://uzumbank.uz")],
        [InlineKeyboardButton(text="🟢 Paynet [ avto ]", url="https://paynet.uz")],
        [InlineKeyboardButton(text="🔵 Oson [ Avto ]", url="https://oson.uz")],
        [InlineKeyboardButton(text="💳 Uzcard / Humo ( karta ) +2% bonus", url="https://payme.uz")],
        [InlineKeyboardButton(text="☎️ Adminga murojaat", url="https://t.me/SardorbekSayitov")]
    ])
    
    text = (
        "🔸 Payme, 🔹 Click, 🍇 Uzum, 🟢 Paynet,\n"
        "🔵 Oson, 🟡 Alif - ilovalariga kiring To'lov\n"
        "bo'limidan *Neo smm* deb qidiring va botdagi\n"
        "ID raqamingizni kiritib to'lov qilish tugmasini\n"
        "bosing.\n\n"
        f"👤 *ID raqam:* {client_id}"
    )
    
    await message.answer(text, reply_markup=pay_buttons, parse_mode="Markdown")
    # --- 7. SOZLANAYOTGAN TUGMALAR JAVOBI ---
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message(F.text == "🛍️ Telegram") # Yoki menyudagi tugmangiz nomi nima bo'lsa, o'shani yozing
async def telegram_menu(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Telegram obunachi", callback_data="tg_subs")],
        [InlineKeyboardButton(text="⭐ Premium obunachi", callback_data="tg_prem")],
        [InlineKeyboardButton(text="📢 Boost hikoyalarga ovoz", callback_data="tg_boost")],
        [InlineKeyboardButton(text="📊 Ovoz | So'rovnoma", callback_data="tg_poll")],
        [InlineKeyboardButton(text="👁️ Prosmotrlar", callback_data="tg_views")],
        [InlineKeyboardButton(text="👍|👎 Reaksiyalar", callback_data="tg_reactions")],
        [InlineKeyboardButton(text="📖 Istoriya ko'rish", callback_data="tg_story")],
        [InlineKeyboardButton(text="🤖 Bot uchun START", callback_data="tg_start")],
        [InlineKeyboardButton(text="✉️ Izohlar + 🔄 Ulashishlar", callback_data="tg_comments")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu")]
    ])
    
    await message.answer("🛍️ Telegram\n\nQuyidagi ichki bo'limlardan birini tanlang:", reply_markup=kb)
# --- BOTNI ISHGA TUSHIRISH ---
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())