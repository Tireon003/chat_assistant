from aiogram import Bot, Dispatcher
import asyncio
import logging

from client.src.handlers import commands_handler, chating_handler
from client.config import settings


logging.basicConfig(level=settings.LOG_LEVEL)


async def main():
    bot = Bot(token=settings.BOT_API_KEY)
    dp = Dispatcher()
    dp.include_router(commands_handler)
    dp.include_router(chating_handler)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
