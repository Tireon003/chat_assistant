from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware
import asyncio
import logging

from client.src.handlers import commands_handler, chating_handler
from client.config import settings


logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)


async def main():
    bot = Bot(token=settings.BOT_API_KEY)
    dp = Dispatcher()
    dp.include_router(commands_handler)
    dp.include_router(chating_handler)
    dp.message.middleware(ChatActionMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
