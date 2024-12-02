from aiogram import Router, types, F

from client.src.api import AgentsAPI

router = Router(name="chating_router")


@router.message(F.text)
async def handle_query_text(message: types.Message) -> None:
    if len(message.text) < 6:
        await message.reply(
            text="Текст запроса слишком короткий (менее 6 символов)!"
        )

    pending_message = await message.reply("Ассистент готовит ответ...")
    answer = await AgentsAPI.send_message(message.text)
    await pending_message.delete()
    await message.reply(text=answer)
