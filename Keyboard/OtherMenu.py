from Functions.USER_activity import user_activity
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, Router, F
from Functions.BOT_settings import TOKEN

dp = Dispatcher()
router4 = Router()
bot = Bot(token=TOKEN, parse_mode="HTML")

@router4.message(F.text == "/language")
async def inline_key_start(call: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='🏳️Старт', callback_data='en')
    builder.button(text='📰Новини', callback_data='uk')
    builder.button(text='💬Чат', callback_data='ru')
    builder.adjust(1)
    await call.answer("Вибери мову інтерфейсу користувача".format(call.from_user),
                                 reply_markup=builder.as_markup())


    RunPerson = user_activity()
    RunPerson.user_location = "Користувач вибира мову інтерфейса"
    RunPerson.last_activity(call)