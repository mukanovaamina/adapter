from coffee_machine import CoffeeMachine
# adapter, that adapt coffee types to CoffeeMachinr
class CoffeeAdapter(CoffeeMachine):
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def brew_coffee(self):
        self.coffee_type.brew()
