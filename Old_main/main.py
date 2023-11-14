from Functions.USER_Profile import profile_info_money_func, profile_info_status_func
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Functions.KUNA_API import parcing, order_manipulation
from Functions.USER_activity import user_activity
from Functions.INPUT_Time import Time_operations
from aiogram import Bot, Dispatcher, types, Router, F
from Functions.BOT_settings import TOKEN
import asyncio
import pygame

bot = Bot(token=TOKEN)
dp = Router()
router = Router()

print("Bot started!\nLog:")
@dp.message(F.TEXT)
async def inline_key(call: types.Message):
    startmenu = InlineKeyboardMarkup(row_width=1)
    start = InlineKeyboardButton(text='🏳️Старт', callback_data='start')
    news = InlineKeyboardButton(text='📰Новини', callback_data='news')
    chat = InlineKeyboardButton(text='💬Чат', callback_data='chat')
    cabinet = InlineKeyboardButton(text='🗄Кабінет', callback_data='cabinet')
    bobrator = InlineKeyboardButton(text='👤Оператор', callback_data='operator')
    balance = InlineKeyboardButton(text='➕Поповнити Баланс💲', callback_data='balance')
    startmenu.add(start, news, chat, cabinet, bobrator, balance)
    await call.answer("👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id} ".format(call.from_user),
                                 reply_markup=startmenu)

    RunPerson = user_activity()
    RunPerson.user_location = "Користувач на початковому меню"
    RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "back")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        start = InlineKeyboardButton(text='🏳️Старт', callback_data='start')
        news = InlineKeyboardButton(text='📰Новини', callback_data='news')
        chat = InlineKeyboardButton(text='💬Чат', callback_data='chat')
        cabinet = InlineKeyboardButton(text='🗄Кабінет', callback_data='cabinet')
        bobrator = InlineKeyboardButton(text='👤Оператор', callback_data='operator')
        balance = InlineKeyboardButton(text='➕Поповнити Баланс💲', callback_data='balance')
        mainmenu.add(start, news, chat, cabinet, bobrator, balance)
        await call.message.edit_text('👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id}'.format(call.from_user),
                                     reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач повернувся на початкове меню"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "news")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(back)
        await call.message.edit_text('Новини: (немає)', reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню новин"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "chat")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text='Наш чат', url='https://www.youtube.com/')
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, back)
        await call.message.edit_text('Чати: ', reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню чатів"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "cabinet")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(back)
        await call.message.edit_text(f'Ваш статус: '+ profile_info_status_func() +'\n' +
                                     'Ваш баланс: ' + profile_info_money_func(), reply_markup=mainmenu,
                                     parse_mode="Markdown")

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в своєму кабінеті"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "operator")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text='👤Оператор', url='https://www.youtube.com/')
        btn2 = InlineKeyboardButton(text='🛠👤Тех. Оператор', url='https://www.youtube.com/')
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, btn2, back)
        await call.message.edit_text('Оператори: ', reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню операторів"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "balance")
async def callback_inline(call: CallbackQuery):
        balance_menu = InlineKeyboardMarkup(row_width=1)
        pay_balance = InlineKeyboardButton(text='➕поповнити баланс💲', callback_data='USD TRC20')
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back_delete')
        balance_menu.add(pay_balance, back)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'

        await call.message.answer_photo("https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=balance_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "back_balance")
async def callback_inline(call: CallbackQuery):
        await call.message.delete()
        balance_menu = InlineKeyboardMarkup(row_width=1)
        pay_balance = InlineKeyboardButton(text='➕поповнити баланс💲', callback_data='USD TRC20')
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back_delete')
        balance_menu.add(pay_balance, back)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'

        await call.message.answer_photo("https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=balance_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "back_delete")
async def callback_inline(call: CallbackQuery):
        await call.message.delete()

@dp.callback_query_handler(lambda call: call.data == "USD TRC20")
async def callback_inline(call: CallbackQuery):
        await call.message.delete()
        complete_pay_menu = InlineKeyboardMarkup(row_width=1)
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору товара', callback_data='back_balance')
        complete_pay_menu.add(back)
        await call.message.answer('\nMи виkopиcтoвуємo куpc ПpивaтБaнку ' + str(parcing()) + ' ГРН'
                                     '\n' +
                                     '\nКуна aдpeca для пoпoвнeння: ' + str(0) +
                                     '\n' +
                                     '\nУвaгa! ми пpиймaємo лишe TRC20 USDT!' +
                                     '\n' +
                                     '\nBci кoшти яki зaйдуть нa aдpecу дo: ' + (Time_operations.show_time_timedelta30()) +
                                     '\nпoтpaплять нa твiй paxунoк.', reply_markup=complete_pay_menu)
        # RunOrder_manipulation = order_manipulation()
        # RunOrder_manipulation.create_order()
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу(В процессі поповнення балансу)"
        RunPerson.last_activity(call)
        await asyncio.sleep(3600)
        # RunOrder_manipulation.cancel_order()
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Час для оплати рахунку був вичерпаний.\nПовторіть спробу...')

@dp.callback_query_handler(lambda call: call.data == "start")
async def callback_inline(call: CallbackQuery):
        mainmenu = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text='🌆Івано-Франківська область🌆', callback_data='btn_Franik')
        back = InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, back)
        await call.message.edit_text('Задай область', reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора областей"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "btn_Franik")
async def callback_inline(call: CallbackQuery):
        Franik_menu = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(
            text='🌆смт.Отинія🌆', callback_data='Otynia')
        btn2 = InlineKeyboardButton(
            text='🌇Угорники(Франківськ)🌇', callback_data='Ugornyky_Franik')
        btn3 = InlineKeyboardButton(
            text='🏙Угорники(Коломия)🏙', callback_data='Ugornyky_Kolomuya')
        btn4 = InlineKeyboardButton(
            text='🌆Івано - Франківськ🌆', callback_data='btn2_Franik')
        btn5 = InlineKeyboardButton(
            text='🌇Коломия🌇', callback_data='Kolomuya')
        back2 = InlineKeyboardButton(
            text='◀️Вернутися до вибору області(ей)', callback_data='start')
        Franik_menu.add(btn1, btn2, btn3, btn4, btn5, back2)
        await call.message.edit_text('Задай Місто/смт./село', reply_markup=Franik_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора Міст/смт./сіл"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "Otynia")
async def callback_inline(call: CallbackQuery):
        tovar_menu = InlineKeyboardMarkup(row_width=1)
        tovar1 = InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        await call.message.edit_text('Вибирай:)', reply_markup=tovar_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Отинія)"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "Ugornyky_Franik")
async def callback_inline(call: CallbackQuery):
        tovar_menu = InlineKeyboardMarkup(row_width=1)
        tovar1 = InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        await call.message.edit_text('Вибирай:)', reply_markup=tovar_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Франківська область)"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "Ugornyky_Kolomuya")
async def callback_inline(call: CallbackQuery):
        tovar_menu = InlineKeyboardMarkup(row_width=1)
        tovar1 = InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        await call.message.edit_text('Вибирай:)', reply_markup=tovar_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Коломийська область)"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "btn2_Franik")
async def callback_inline(call: CallbackQuery):
        tovar_menu = InlineKeyboardMarkup(row_width=1)
        tovar1 = InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        await call.message.edit_text('Вибирай:)', reply_markup=tovar_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Франківськ)"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "Kolomuya")
async def callback_inline(call: CallbackQuery):
        tovar_menu = InlineKeyboardMarkup(row_width=1)
        tovar1 = InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сіл', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        await call.message.edit_text('Вибирай:)', reply_markup=tovar_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Коломия)"
        RunPerson.last_activity(call)

@dp.callback_query_handler(lambda call: call.data == "pivo+gorishki")
async def callback_inline(call: CallbackQuery):
        pay_menu = InlineKeyboardMarkup(row_width=1)
        oplata_variantA = InlineKeyboardButton(
            text='✅Підтвердити✅', callback_data='Accept_pivo+gorishki')
        back = InlineKeyboardButton(
            text='◀️Вернутися до вибору товара', callback_data='back_delete')
        pay_menu.add(oplata_variantA, back)
        pivo_gorishki_content = f'Вміст📦\nПиво: 90 мілілітрів\nГорішки: 50 грамм\nЦіна: .'
        await call.message.answer_photo('https://cdn.segodnya.ua/img/article/10156/63_main_new.1493069986.jpg', pivo_gorishki_content, reply_markup=pay_menu)

        RunPerson = user_activity()
        RunPerson.user_location = 'Користувач в меню інформації про товар: Пиво і горішки(Коломия)'
        RunPerson.last_activity(call)

try:
    pass
except Exception:
    pygame.mixer.init()
    pygame.mixer.music.load('exeption_sound.mp3')
    pygame.mixer.music.play(0)
