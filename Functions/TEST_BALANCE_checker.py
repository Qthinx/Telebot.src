

class Tovar_price:
    def __init__(self):            
        self.__tovar_name = "None"
        self.__location = "None" 
        self.__price = 0                      
        self.__gramm = 0.0   
                 

    @property
    def get_tovar_name(self):
        return self.__tovar_name
    
    @property
    def get_tovar_location (self):
        return self.__location  
    
    @property
    def get_tovar_price(self):
        return self.__price 
    
    @property
    def get_tovar_gramm(self):
        return self.__gramm
    
    @get_tovar_name.setter
    def set_tovar_name(self, tovar_name):
        self.__tovar_name = tovar_name

    @get_tovar_gramm.setter
    def set_tovar_gramm(self, location):
        self.__location = location         
        
    @get_tovar_price.setter
    def set_tovar_price(self, price):
        self.__price = price  
        
    @get_tovar_gramm.setter
    def set_tovar_gramm(self, gramm):
        self.__gramm = gramm                
   
    def change_tovar(self, tovar_name, location):     
        if tovar_name == "пиво і горішки":
            self.__tovar_name = "Гоп"   
            self.__location = location                  
            self.__price = 1             
            self.__gramm = 0.1 
                                
         

