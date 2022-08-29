from Tutorial_28Chef import Chef

class ChineseChef(Chef): #Inheret from Chef lets say that our chinese chef can do everything that the generic chef can

    def make_special_dish(self): #Overwriting Chef's special dish
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")