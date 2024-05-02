import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from tokken import BOT_TOKKEN



logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKKEN, parse_mode='HTML')

dp = Dispatcher()

@dp.message(Command('start')) 
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'<b>Привет! Добро пожаловать в @MyIdusername_bot!\n\nСправка: /help\n\nТвой ID: <code>{message.from_user.id}</code>\n\nИмя: <code>{message.from_user.first_name}</code>\n\nФамилия: <code>{message.from_user.last_name}</code></b>')
    

# @dp.message(Command('/help'))
# async def yordam(mesage: types.message):
#     await bot.send_message("Админ: @pragrammer_uz\n")

@dp.message(F.text=='/help')
async def yordam(message: types.Message):
    await bot.send_message(message.chat.id, "Админ: @pragrammer_uz\n")




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot ish faolyatini tugatdi!")
