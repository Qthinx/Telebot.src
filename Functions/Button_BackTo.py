from aiogram import F
class BackTo_():
    def __init__(self):
        self.__BackTo_adress = "Kolomuya"

    @property
    def get_adress(self):
        return self.__BackTo_adress
    
    @get_adress.setter
    def get_adress(self, BackTo_adress):
        self.__BackTo_adress = BackTo_adress

    def get_adress_block(self):
        if self.__BackTo_adress == "Otynia":
            self.__BackTo_adress = "Otynia"
        if self.__BackTo_adress == "Ugornyky_Franik":
            self.__BackTo_adress = "Ugornyky_Franik"
        if self.__BackTo_adress == "Ugornyky_Kolomuya":
            self.__BackTo_adress = "Ugornyky_Kolomuya"
        if self.__BackTo_adress == "Franik":
            self.__BackTo_adress = "Franik"
        if self.__BackTo_adress == "Kolomuya":
            self.__BackTo_adress = "Kolomuya"
