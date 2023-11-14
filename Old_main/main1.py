from Functions.KUNA_API import parcing
from Functions.INPUT_Time import Time_operations
from Functions.USER_Profile import profile_info_money_func, profile_info_status_func
from telebot import types
from Functions.BOT_settings import ABETKA, bot
from Functions.USER_activity import user_activity
import time


print("Bot started!\nLog:")
@bot.message_handler(content_types=['text'])
def inline_key(call):
    if call.text in ABETKA:

        startmenu = types.InlineKeyboardMarkup(row_width=1)
        start = types.InlineKeyboardButton(text='🏳️Старт', callback_data='start')
        news = types.InlineKeyboardButton(text='📰Новини', callback_data='news')
        chat = types.InlineKeyboardButton(text='💬Чат', callback_data='chat')
        cabinet = types.InlineKeyboardButton(text='🗄Кабінет', callback_data='cabinet')
        bobrator = types.InlineKeyboardButton(text='👤Оператор', callback_data='operator')
        balance = types.InlineKeyboardButton(text='➕Поповнити Баланс💲', callback_data='balance')
        startmenu.add(start, news, chat, cabinet, bobrator, balance)
        bot.send_message(call.chat.id,text="👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id} ".format(call.from_user),
                     reply_markup=startmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач на початковому меню"
        RunPerson.last_activity(call)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "back":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        start = types.InlineKeyboardButton(text='🏳️Старт', callback_data='start')
        news = types.InlineKeyboardButton(text='📰Новини', callback_data='news')
        chat = types.InlineKeyboardButton(text='💬Чат', callback_data='chat')
        cabinet = types.InlineKeyboardButton(text='🗄Кабінет', callback_data='cabinet')
        bobrator = types.InlineKeyboardButton(text='👤Оператор', callback_data='operator')
        balance = types.InlineKeyboardButton(text='➕Поповнити Баланс💲', callback_data='balance')
        mainmenu.add(start, news, chat, cabinet, bobrator, balance)
        bot.edit_message_text('👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id}'.format(
            call.from_user), call.message.chat.id, call.message.message_id,
            reply_markup=mainmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач повернувся на початкове меню"
        RunPerson.last_activity(call)

    elif call.data == "back":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        start = types.InlineKeyboardButton(text='🏳️Старт', callback_data='start')
        news = types.InlineKeyboardButton(text='📰Новини', callback_data='news')
        chat = types.InlineKeyboardButton(text='💬Чат', callback_data='chat')
        cabinet = types.InlineKeyboardButton(text='🗄Кабінет', callback_data='cabinet')
        bobrator = types.InlineKeyboardButton(text='👤Оператор', callback_data='operator')
        balance = types.InlineKeyboardButton(text='➕Поповнити Баланс💲', callback_data='balance')
        mainmenu.add(start, news, chat, cabinet, bobrator, balance)
        bot.edit_message_text('👨‍💻Привіт, {0.username}\n🔢Ваш id: {0.id}'.format(
            call.from_user), call.message.chat.id, call.message.message_id,
            reply_markup=mainmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач повернувся на початкове меню"
        RunPerson.last_activity(call)

    if call.data == "news":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(back, )
        bot.edit_message_text(
            'Новини: (немає)',
            call.message.chat.id,
            call.message.message_id,
            reply_markup=mainmenu
        )

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню новин"
        RunPerson.last_activity(call)
        
    elif call.data == "chat":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Наш чат', url='https://www.youtube.com/')
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, back, )
        bot.edit_message_text('Чати: ', call.message.chat.id, call.message.message_id,
                              reply_markup=mainmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню чатів"
        RunPerson.last_activity(call)
        
    elif call.data == "cabinet":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='◀️Вернутия на початок', callback_data='back')
        mainmenu.add(back, )
        bot.edit_message_text(f'Ваш статус: '+ profile_info_status_func() +'\n' +
                              'Ваш баланс: ' + profile_info_money_func() + ' UAH', call.message.chat.id, call.message.message_id, parse_mode="Markdown",
                              reply_markup=mainmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в своєму кабінеті"
        RunPerson.last_activity(call)
        
    elif call.data == "operator":
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='👤Оператор', url='https://www.youtube.com/')
        btn2 = types.InlineKeyboardButton(text='🛠👤Тех. Оператор', url='https://www.youtube.com/')
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, btn2, back, )
        bot.edit_message_text('Оператори: ', call.message.chat.id, call.message.message_id,
                              reply_markup=mainmenu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню операторів"
        RunPerson.last_activity(call)
        
    elif call.data == "balance":
        balance_menu = types.InlineKeyboardMarkup(row_width=1)
        pay_balance = types.InlineKeyboardButton(text='➕поповнити баланс💲', callback_data='USD TRC20')
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back_delete')
        balance_menu.add(pay_balance, back)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'
        
        bot.send_photo(call.message.chat.id, "https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=balance_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)
        
    elif call.data == "back_balance":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        balance_menu = types.InlineKeyboardMarkup(row_width=1)
        pay_balance = types.InlineKeyboardButton(text='➕поповнити баланс💲', callback_data='USD TRC20')
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back_delete')
        balance_menu.add(pay_balance, back)
        s = 'ㅤㅤㅤㅤㅤ📒Інструкція📒ㅤㅤㅤㅤ\n1.Йди нахуй.'
        
        bot.send_photo(call.message.chat.id, "https://img2.joyreactor.cc/pics/post/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-7212041.jpeg", s, reply_markup=balance_menu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу"
        RunPerson.last_activity(call)
        
    elif call.data == "back_delete":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    elif call.data == "USD TRC20":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        complete_pay_menu = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору товара', callback_data='back_balance')
        complete_pay_menu.add(back)
        bot.send_message(call.message.chat.id, reply_markup=complete_pay_menu, text = '\nMи виkopиcтoвуємo куpc ПpивaтБaнку ' + str(parcing()) + ' ГРН'
                                     '\n' +
                                     '\nКуна aдpeca для пoпoвнeння: ' + str(0()) +
                                     '\n' +
                                     '\nУвaгa! ми пpиймaємo лишe TRC20 USDT!' +
                                     '\n' +
                                     '\nBci кoшти яki зaйдуть нa aдpecу дo: ' + (Time_operations.show_time_timedelta30()) +
                                     '\n' +
                                     '\nпoтpaплять нa твiй paxунoк.')
        
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню поповнення балансу(В процессі поповнення)"
        RunPerson.last_activity(call)
        time.sleep(3600)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text='Час для оплати рахунку був вичерпаний.\nПовторіть спробу...')     

    elif call.data == "start":
        
        mainmenu = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='🌆Івано-Франківська область🌆', callback_data='btn_Franik')
        back = types.InlineKeyboardButton(text='◀️Вернутися на початок', callback_data='back')
        mainmenu.add(btn1, back, )
        bot.edit_message_text('Задай область', call.message.chat.id, call.message.message_id, 
            reply_markup=mainmenu)

        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора областей"
        RunPerson.last_activity(call)
        
    elif call.data == "btn_Franik":
        Franik_menu = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(
            text='🌆смт.Отинія🌆', callback_data='Otynia')
        btn2 = types.InlineKeyboardButton(
            text='🌇Угорники(Франківськ)🌇', callback_data='Ugornyky_Franik')
        btn3 = types.InlineKeyboardButton(
            text='🏙Угорники(Коломия)🏙', callback_data='Ugornyky_Kolomuya')
        btn4 = types.InlineKeyboardButton(
            text='🌆Івано - Франківськ🌆', callback_data='btn2_Franik')
        btn5 = types.InlineKeyboardButton(
            text='🌇Коломия🌇', callback_data='Kolomuya')
        back2 = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору області(ей)', callback_data='start')
        Franik_menu.add(btn1, btn2, btn3, btn4, btn5, back2)
        bot.edit_message_text('Задай Місто/смт./село', call.message.chat.id, call.message.message_id,
                              reply_markup=Franik_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора Міст/смт./сіл"
        RunPerson.last_activity(call)
        
    elif call.data == "Otynia":
        tovar_menu = types.InlineKeyboardMarkup(row_width=1)
        tovar1 = types.InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        bot.edit_message_text('Вибирай:)', call.message.chat.id, call.message.message_id,
                              reply_markup=tovar_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Отинія)"
        RunPerson.last_activity(call)
        
    elif call.data == "Ugornyky_Franik":
        tovar_menu = types.InlineKeyboardMarkup(row_width=1)
        tovar1 = types.InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        bot.edit_message_text('Вибирай:)', call.message.chat.id, call.message.message_id,
                              reply_markup=tovar_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Франківська область)"
        RunPerson.last_activity(call)
        
    elif call.data == "Ugornyky_Kolomuya":
        tovar_menu = types.InlineKeyboardMarkup(row_width=1)
        tovar1 = types.InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        bot.edit_message_text('Вибирай:)', call.message.chat.id, call.message.message_id,
                              reply_markup=tovar_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Угорники, Коломийська область)"
        RunPerson.last_activity(call)
        
    elif call.data == "btn2_Franik":
        tovar_menu = types.InlineKeyboardMarkup(row_width=1)
        tovar1 = types.InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сел', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        bot.edit_message_text('Вибирай:)', call.message.chat.id, call.message.message_id,
                              reply_markup=tovar_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Франківськ)"
        RunPerson.last_activity(call)

    elif call.data == "Kolomuya":
        tovar_menu = types.InlineKeyboardMarkup(row_width=1)
        tovar1 = types.InlineKeyboardButton(
            text='🍺пиво🍺 і 🥜горішки🥜', callback_data='pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору Міст/смт./сіл', callback_data='btn_Franik')
        tovar_menu.add(tovar1, back)
        bot.edit_message_text('Вибирай:)', call.message.chat.id, call.message.message_id,
                              reply_markup=tovar_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = "Користувач в меню вибора товара(Коломия)"
        RunPerson.last_activity(call)

    elif call.data == "pivo+gorishki":
        pay_menu = types.InlineKeyboardMarkup(row_width=1)
        oplata_variantA = types.InlineKeyboardButton(
            text='✅Підтвердити✅', callback_data='Accept_pivo+gorishki')
        back = types.InlineKeyboardButton(
            text='◀️Вернутися до вибору товара', callback_data='back_delete')
        pay_menu.add(oplata_variantA, back)
        pivo_gorishki_content =f'Вміст📦\nПиво: 90 мілілітрів\nГорішки: 50 грамм\nЦіна: .'
        bot.send_photo(call.message.chat.id, 'https://cdn.segodnya.ua/img/article/10156/63_main_new.1493069986.jpg', pivo_gorishki_content,
                              reply_markup=pay_menu)
        
        RunPerson = user_activity()
        RunPerson.user_location = 'Користувач в меню інформації про товар: Пиво і горішки(Коломия)'
        RunPerson.last_activity(call)
        

while True:
    try:
        bot.polling(non_stop=True)
    except Exception:
        # Обробка помилок та перезапуск бота при необхідності
        pass
