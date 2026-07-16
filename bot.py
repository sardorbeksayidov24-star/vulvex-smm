import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Botingizning tokenini shu yerga yozing
TOKEN = "8835809644:AAFapOaMC8SXgxISGTq7Jz9huCmLYLO7oAU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Bot muvaffaqiyatli ishga tushdi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
