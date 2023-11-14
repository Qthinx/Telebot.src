from aiogram.utils.keyboard import InlineKeyboardBuilder
from Functions.TEST_BALANCE_checker import Tovar_price
from Functions.USER_activity import user_activity
from aiogram import Bot, Dispatcher, Router, F
from Functions.BOT_settings import TOKEN

dp = Dispatcher()
router3 = Router()
bot = Bot(token=TOKEN, parse_mode="HTML")
tom = Tovar_price()
    
@router3.callback_query(F.data == "Otynia")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()           
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Отинія/Otynia')       
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.edit_text('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Отинія)"
        RunPerson.last_activity(call)           
            
@router3.callback_query(F.data == "Ugornyky_Franik")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Угорники, Франківська область/Ugornyky_Franik')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.edit_text('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Франківська область)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "Ugornyky_Kolomuya")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Угорники, Коломийська область/Ugornyky_Kolomuya')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.edit_text('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Коломийська область)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "btn2_Franik")
async def callback_inline(call):
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Франківськ/btn2_Franik')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.edit_text('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Франківськ)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "Kolomuya")
async def callback_inline(call):
        tom.change_tovar("None", call.data)        
        builder = InlineKeyboardBuilder()       
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Коломия/Kolomuya')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сіл', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.edit_text('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Коломия)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data.startswith("пиво і горішки/"))
async def callback_inline(call):                
        await call.message.delete()
        ddata = call.data   
        while "/" in ddata:
                text = ddata.split("/", 2)
                break
        tom.change_tovar(text[0], text[1])
        builder = InlineKeyboardBuilder()
        builder.button(text='✅Підтвердити✅', callback_data='Accept_pivo+gorishki')
        builder.button(text='◀️Вернутися до вибору товара', callback_data=f'back_{text[2]}')
        builder.adjust(1)
        pivo_gorishki_content = f'Вміст📦\nНазва: {tom.get_tovar_name}\nВага: {tom.get_tovar_gramm} грамм\nЦіна: {tom.get_tovar_price}'
        await call.message.answer_photo('https://cdn.segodnya.ua/img/article/10156/63_main_new.1493069986.jpg', pivo_gorishki_content, reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = f'Користувач в меню інформації про товар: Пиво і горішки({tom.get_tovar_location})'
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "Accept_pivo+gorishki")
async def callback_inline(call):
        user_id = '5552883871'           
        await bot.send_message(user_id, "Привіт! Це тестове повідомлення для курєра.")

@router3.callback_query(F.data == "back_Otynia")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()           
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Отинія/Otynia')       
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.answer('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Отинія)"
        RunPerson.last_activity(call)           
            
@router3.callback_query(F.data == "back_Ugornyky_Franik")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Угорники, Франківська область/Ugornyky_Franik')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.answer('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Франківська область)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "back_Ugornyky_Kolomuya")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Угорники, Коломийська область/Ugornyky_Kolomuya')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.answer('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Коломийська область)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "back_btn2_Franik")
async def callback_inline(call):
        await call.message.delete()
        builder = InlineKeyboardBuilder()
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Франківськ/btn2_Franik')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.answer('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Франківськ)"
        RunPerson.last_activity(call)

@router3.callback_query(F.data == "back_Kolomuya")
async def callback_inline(call):
        await call.message.delete()       
        builder = InlineKeyboardBuilder()       
        builder.button(text='🍺пиво🍺 і 🥜горішки🥜', callback_data='пиво і горішки/Коломия/Kolomuya')
        builder.button(text='◀️Вернутися до вибору Міст/смт./сіл', callback_data='btn_Franik')
        builder.adjust(1)
        await call.message.answer('Вибирай:)', reply_markup=builder.as_markup())

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Коломия)"
        RunPerson.last_activity(call)
                                 