from datetime import datetime, timedelta
# Виведення часу
class Time_operations():

    def show_time_timedelta30():
        return (datetime.now() + timedelta(minutes=30)).strftime("%H:%M:%S")

    def show_current_advanced_time():
        return datetime.now().strftime("%d.%m.%Y|%H:%M:%S")
    
    def show_current_time():
        return datetime.now()
    
###