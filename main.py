from coffee_machine import CoffeeMachine
from coffee_types import Espresso, Latte
from coffee_adapter import CoffeeAdapter
from coffee_shop import CoffeeShop

# creating objects for coffeemachine, types of coffee, adapter and client.
coffee_machine = CoffeeMachine()
espresso = Espresso()
latte = Latte()
espresso_adapter = CoffeeAdapter(espresso)
latte_adapter = CoffeeAdapter(latte)

# Create object CoffeeShop and use it for making types of coffee
coffee_shop = CoffeeShop()
coffee_shop.serve_coffee(coffee_machine)       # Making coffee
coffee_shop.serve_coffee(espresso_adapter)    # Making Espresso
coffee_shop.serve_coffee(latte_adapter)        # Making Lattr
