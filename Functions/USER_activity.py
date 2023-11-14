from Functions.USER_Profile import profile_info_money_func, profile_info_status_func
from Functions.INPUT_Time import Time_operations
from DataBase.DataBase import db_table_val



previous_name = None
previous_nickname = None
nickname_in_log = None

def write_in_db(call):
    id = call.from_user.id 
    name = call.from_user.first_name 
    nickname = call.from_user.username 
    status = profile_info_status_func()
    balance = profile_info_money_func()
    activity = nickname_in_log
    print(activity)
    bot_log = open("bot_log.txt", "a")
    bot_log.write(activity + "\n ")    
    db_table_val(user_id=id, user_name=name, user_nickname=nickname, user_status=status, user_balance=balance, user_last_activity=activity)

class user_activity:
    def __init__(self):
        self.__user_location = "Незнаю" 
    

    @property
    def user_location(self):
        return self.__user_location
    
    @user_location.setter
    def user_location(self, user_location):
        self.__user_location = user_location

    def last_activity(self, call):
        global previous_nickname, previous_name, nickname_in_log
            
        if call.from_user.username is None:
            call.from_user.username = "Немає"

        if previous_nickname is None:
            previous_nickname = call.from_user.username

        if previous_name is None:
            previous_name = call.from_user.first_name

        if previous_nickname == call.from_user.username or previous_name == call.from_user.first_name:
            nickname_in_log = f"Нікнейм: {call.from_user.username}\nІм'я: {call.from_user.first_name}\nID: {call.from_user.id}\n{self.__user_location}({Time_operations.show_current_advanced_time()})\n"
            write_in_db(call)

        if call.from_user.username != previous_nickname and call.from_user.first_name != previous_name:
            nickname_in_log = f"Нікнейм: {call.from_user.username} (попередній нікнейм: {previous_nickname})\nІм'я: {call.from_user.first_name} (попереднє ім'я: {previous_name})\nID: {call.from_user.id}\n{self.__user_location}({Time_operations.show_current_advanced_time()})\n"
            write_in_db(call)
            
        elif call.from_user.username != previous_nickname:
            nickname_in_log = f"Нікнейм: {call.from_user.username} (попередній нікнейм: {previous_nickname})\nІм'я: {call.from_user.first_name}\nID: {call.from_user.id}\n{self.__user_location}({Time_operations.show_current_advanced_time()})\n"
            write_in_db(call)
            
        elif call.from_user.first_name != previous_name:
            nickname_in_log = f"Нікнейм: {call.from_user.username}\nІм'я: {call.from_user.first_name} (попереднє ім'я: {previous_name})\nID: {call.from_user.id}\n{self.__user_location}({Time_operations.show_current_advanced_time()})\n"
            write_in_db(call)
            
        previous_nickname = call.from_user.username
        previous_name = call.from_user.first_name
        return nickname_in_log
    