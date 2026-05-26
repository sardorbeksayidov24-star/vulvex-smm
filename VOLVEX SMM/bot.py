import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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
    
    # Karta raqamingiz va ismingizni shu yerga aniq yozing:
    KARTA_RAQAM = "8600123456789012"  # O'zingizning karta raqamingizni yozing
    KARTA_NOMI = "Sardorbek S."       # Karta egasining ismi
    
    pay_buttons = InlineKeyboardMarkup(inline_keyboard=[
        # Payme orqali to'g'ridan-to'g'ri kartangizga o'tkazish tugmasi
        [InlineKeyboardButton(text="💳 Karta orqali (Payme P2P)", url=f"https://payme.uz/p2p/{KARTA_RAQAM}")],
        # Avto-to'lov tizimlari havolalari
        [InlineKeyboardButton(text="🔸 Payme [ Avto-Neo SMM ]", url=f"https://payme.uz/fallback/paynet/search?keyword=Neo+smm&id={client_id}")],
        [InlineKeyboardButton(text="🔹 Click [ Avto ]", url="https://click.uz")],
        [InlineKeyboardButton(text="🍇 Uzum [ Avto ] +2% bonus", url="https://uzumbank.uz")],
        [InlineKeyboardButton(text="🟢 Paynet [ avto ]", url="https://paynet.uz")],
        [InlineKeyboardButton(text="☎️ Adminga chek yuborish", url="https://t.me/SardorbekSayitov")]
    ])
    
    text = (
        "👋 *Hisobni to'ldirish bo'limiga xush kelibsiz!*\n\n"
        "💳 1-USUL: KАRTАGА TO'G'RIDАN-TO'G'RI O'TKАZISH\n"
        "Pastdagi karta raqamiga pul o'tkazing:\n\n"
        f"📌 *Karta raqam:* {KARTA_RAQAM}\n"
        f"👤 *Ega:* {KARTA_NOMI}\n\n"
        "⚠️ *Muhim:* Pulni o'tkazgach, chekni (skrinshot) va botdagi "
        "ID raqamingizni '☎️ Adminga chek yuborish' tugmasi orqali adminga yuboring. "
        "Balansingiz tezda yangilanadi.\n\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "🟢 2-USUL: ILОВАLАR ORQАLI (АVTO)\n"
        "Payme, Click, Uzum yoki Paynet ilovalariga kiring.\n"
        "To'lov bo'limidan 'Neo smm' deb qidiring va\n"
        "botdagi ID raqamingizni kiritib to'lov qiling.\n\n"
        f"👤 *Sizning ID raqamingiz:* {client_id}"
    )
    
    await message.answer(text, reply_markup=pay_buttons, parse_mode="Markdown")
    
    await message.answer(text, reply_markup=pay_buttons, parse_mode="Markdown")
    # --- 7. SOZLANAYOTGAN TUGMALAR JAVOBI ---
@dp.message(F.text.in_({
    "🎮 Pubg Uc", "🎮 Free Fire Almaz", "🎮 Mobile Legends",
    "🛍️ Telegram", "🛍️ Instagram", "🛍️ Tik Tok", "🛍️ You tube", "🛍️ Facebook", "🛍️ Threads", "⭐ Premium, Starts, Gift",
    "👥 Referal", "📊 Buyurtmalarim", "📕 Qo'llanma", "☎️ Qo'llab-quvvatlash", "🤝 Hamkorlik dasturi"
}))
async def placeholder_commands(message: types.Message):
    await message.answer(f"⚙️ {message.text} bo'limi hozirda sozlanmoqda. Tez orada to'liq ishga tushadi!")

# --- BOTNI ISHGA TUSHIRISH ---
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())