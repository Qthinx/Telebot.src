
from Keyboard.CityTownVillage_chooseMenu import router2
from Keyboard.PayTovar_Menus import router3
from aiogram import Bot, Dispatcher, Router
from Functions.BOT_settings import TOKEN
from Keyboard.StartMenu import router1
from Keyboard.OtherMenu import router4 
import asyncio
import pygame

dp = Dispatcher()
router = Router()
bot = Bot(token=TOKEN, parse_mode="HTML")  
 
print("Bot started!\nLog:")

router.include_router(router4)
router.include_router(router1)
router.include_router(router2)
router.include_router(router3)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
try:
    pass
except Exception:
    pygame.mixer.init()
    pygame.mixer.music.load('exception_sound.mp3')
    pygame.mixer.music.play(0)
