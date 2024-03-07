from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
import asyncio
import logging
from core.settings import settings


async def on_startup(bot: Bot):
    await bot.send_message(settings.bots.ADMIN_ID, text='Bot is running')


async def on_shutdown(bot: Bot):
    await bot.send_message(settings.bots.ADMIN_ID, text='Bot shut down')

async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message).'
                        )
    bot = Bot(token=settings.bots.BOT_TOKEN, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())