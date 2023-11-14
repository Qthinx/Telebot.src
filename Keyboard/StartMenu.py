from Functions.USER_Profile import profile_info_money_func, profile_info_status_func
from Functions.KUNA_API import parcing
from Functions.USER_activity import user_activity
from Functions.INPUT_Time import Time_operations
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, Router, F
from Functions.BOT_settings import TOKEN
import asyncio

dp = Dispatcher()
router1 = Router()
bot = Bot(token=TOKEN, parse_mode="HTML")

@router1.message()
async def inline_key_start(call: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='🏳️Старт', callback_data='start')
    builder.button(text='📰Новини', callback_data='news')             
    builder.button(text='💬Чат', callback_data='chat')
    builder.button(text='🗄Кабінет', callback_data='cabinet')
    builder.button(text='👤Оператор', callback_data='operator')
    builder.button(text='➕Поповнити Баланс💲', callback_data='balance')
    builder.adjust(1)          

    await call.answer("👨‍💻Привіт, {0.full_name}\n🔢Ваш id: {0.id} ".format(call.from_user),
                                 reply_markup=builder.as_markup())

    RunPerson = user_activity()
    RunPerson.user_location = "Користувач на початковому меню"
    RunPerson.last_activity(call)
    
@router1.callback_query(F.data == "back")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🏳️Старт', callback_data='start')
        builder.button(text='📰Новини', callback_data='news')               
        builder.button(text='💬Чат', callback_data='chat')
        builder.button(text='🗄Кабінет', callback_data='cabinet')
        builder.button(text='👤Оператор', callback_data='operator')
        builder.button(text='➕Поповнити Баланс💲', callback_data='balance')
        builder.adjust(1) 
        
        await call.message.edit_text('👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id}'.format(call.from_user),
                                     reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач повернувся на початкове меню"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "news")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='◀️Вернутися на початок', callback_data='back')
        builder.adjust(1)
        await call.message.edit_text('Новини: (немає)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню новин"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "chat")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='Наш чат', url='https://www.youtube.com/')
        builder.button(text='◀️Вернутися на початок', callback_data='back')
        builder.adjust(1)
        await call.message.edit_text('Чати: ', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню чатів"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "cabinet")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='◀️Вернутися на початок', callback_data='back')
        builder.adjust(1)
        await call.message.edit_text(f'Ваш статус: '+ profile_info_status_func() +'\n' +
                                     'Ваш баланс: ' + profile_info_money_func(), reply_markup=builder.as_markup(),
                                     parse_mode="Markdown")

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в своєму кабінеті"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "operator")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='👤Оператор', url='https://www.youtube.com/')
        builder.button(text='🛠👤Тех. Оператор', url='https://www.youtube.com/')
        builder.button(text='◀️Вернутися на початок', callback_data='back')
        builder.adjust(1)
        await call.message.edit_text('Оператори: ', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню операторів"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "balance")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='➕поповнити баланс💲', callback_data='USD TRC20')
        builder.button(text='◀️Вернутися на початок', callback_data='back_delete_in_menu')
        builder.adjust(1)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'

        await call.message.answer_photo("https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "back_balance")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='➕поповнити баланс💲', callback_data='USD TRC20')
        builder.button(text='◀️Вернутися на початок', callback_data='back_delete_in_menu')
        builder.adjust(1)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'

        await call.message.answer_photo("https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "back_delete")
async def callback_inline(call):
        await call.message.delete()

@router1.callback_query(F.data == "back_delete_in_menu")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='🏳️Старт', callback_data='start')
        builder.button(text='📰Новини', callback_data='news')
        builder.button(text='💬Чат', callback_data='chat')
        builder.button(text='🗄Кабінет', callback_data='cabinet')
        builder.button(text='👤Оператор', callback_data='operator')
        builder.button(text='➕Поповнити Баланс💲', callback_data='balance')
        builder.adjust(1)
        await call.message.answer("👨‍💻Привіт, {0.full_name}\n🔢Ваш id: {0.id}".format(call.from_user),
                                    reply_markup=builder.as_markup())


        RunPerson = user_activity()
        RunPerson.user_location = "Користувач на початковому меню"
        RunPerson.last_activity(call)

@router1.callback_query(F.data == "USD TRC20")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='◀️Вернутися до вибору товара', callback_data='back_balance')
        builder.adjust(1)
        await call.message.answer('\nMи виkopиcтoвуємo куpc ПpивaтБaнку ' + str(parcing()) + ' ГРН'
                                     '\n' +
                                     '\nКуна aдpeca для пoпoвнeння: ' + str(0) +
                                     '\n' +
                                     '\nУвaгa! ми пpиймaємo лишe TRC20 USDT!' +
                                     '\n' +
                                     '\nBci кoшти яki зaйдуть нa aдpecу дo: ' + (Time_operations.show_time_timedelta30()) +
                                     '\nпoтpaплять нa твiй paxунoк.', reply_markup=builder.as_markup())
        
        # RunOrder_manipulation = order_manipulation()
        # RunOrder_manipulation.create_order()
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу(В процессі поповнення балансу)"
        RunPerson.last_activity(call)
        await asyncio.sleep(3600)
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Час для оплати рахунку був вичерпаний.\nПовторіть спробу...')