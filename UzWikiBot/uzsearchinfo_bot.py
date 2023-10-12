import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6563599732:AAGL65uBlv8vfjQWTefhGg2P1mOB24nugdo'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("UzSearchInfoBotga Xush kelibsiz!")

@dp.message_handler()
async def send_info(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

















