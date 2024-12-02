from aiogram import Router, types
from aiogram.filters import Command

router = Router(name='commands_router')


@router.message(Command("start"))
async def handle_start_command(message: types.Message) -> None:
    await message.reply(
        f"Привет, {message.from_user.full_name}!\n\n"
        f"Данный бот поможет тебе приготовить любое блюдо. В твоем распоряжении есть ассистенты:\n\n"
        f" - Механик: ассистент для поддержки в сфере механики\n"
        f" - Фитнес-тренер: ассистентдля поддержки в сфере тренировок, ПП, ЗОЖ, реабилитации.\n"
        f"\n"
        f"Как работает бот:"
        f"1. Главный агент (менеджер) получает вопрос."
        f"2. Менеджер определяет тематику вопроса и выбирает подходящего агента."
        f"3. Перенаправляет вопрос подходящему агенту."
        f"4. Подходящий агент отввечает на вопрос."
    )
