import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
from handlers import common, celebration_choice

async def main():

    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(celebration_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())