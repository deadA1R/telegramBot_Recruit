import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from APP.handlers_recruit import router_recruit
from APP.handlers_basic import router_basic
from APP.handlers_user import router_usr
from APP.database.models import async_main



async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router_recruit)
    dp.include_router(router_basic)
    dp.include_router(router_usr)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # stop on prod
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")