from Functions.USER_activity import user_activity
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, Router, F
from Functions.BOT_settings import TOKEN

dp = Dispatcher()
router2 = Router()
bot = Bot(token=TOKEN, parse_mode="HTML")

@router2.callback_query(F.data == "start")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🌆Івано-Франківська область🌆', callback_data='btn_Franik')
        builder.button(text='◀️Вернутися на початок', callback_data='back')
        builder.adjust(1)
        await call.message.edit_text('Задай область', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора областей"
        RunPerson.last_activity(call)

@router2.callback_query(F.data == "btn_Franik")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🌆смт.Отинія🌆', callback_data='Otynia')
        builder.button(text='🌇Угорники(Франківськ)🌇', callback_data='Ugornyky_Franik')
        builder.button(text='🏙Угорники(Коломия)🏙', callback_data='Ugornyky_Kolomuya')
        builder.button(text='🌆Івано - Франківськ🌆', callback_data='btn2_Franik')
        builder.button(text='🌇Коломия🌇', callback_data='Kolomuya')
        builder.button(text='◀️Вернутися до вибору області(ей)', callback_data='start')
        builder.adjust(1)
        await call.message.edit_text('Задай Місто/смт./село', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора Міст/смт./сіл"
        RunPerson.last_activity(call)

