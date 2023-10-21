class CoffeeType: #abstract class
    def brew(self):
        pass

class Espresso(CoffeeType): #type of coffee
    def brew(self):
        print("Making Espresso")

class Latte(CoffeeType): #type of coffee
    def brew(self):
        print("Making Latte")
