import aiohttp


class AgentsAPI:

    @staticmethod
    async def send_message(message: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url="http://localhost:8000/api/v1/messages/",
                json=dict(
                    message=message,
                ),
            ) as response:
                if response.status == 200:
                    return (await response.json())["message"]
                if response.status == 422:
                    return "Длина запроса должна быть не менее 6 символов!"
                else:
                    return "Возникла ошибка на стороне сервера!"
