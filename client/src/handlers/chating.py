from aiogram import Router, types, F, flags

from client.src.api import AgentsAPI

router = Router(name="chating_router")


@router.message(F.text)
@flags.chat_action("typing")
async def handle_query_text(message: types.Message) -> None:
    if len(message.text) < 6:
        return await message.reply(
            text="Текст запроса слишком короткий (менее 6 символов)!"
        )

    answer = await AgentsAPI.send_message(message.text)
    await message.reply(text=answer)
