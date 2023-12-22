import asyncio
import logging

from aiogram import Bot, Dispatcher

from envsetup import Credentials
from handlers import  user_handlers

logging.basicConfig(level=logging.INFO)


# Функция конфигурирования и запуска бота
async def main():
    # Инициализируем бот и диспетчер
    bot = Bot(token=Credentials.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot, allowed_updates=[])


if __name__ == '__main__':
    asyncio.run(main())
