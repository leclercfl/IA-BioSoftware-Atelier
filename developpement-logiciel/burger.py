import os
import time
from datetime import datetime

INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}

def get_order_timestamp():
    return str(datetime.now())

def GetBun():
    bun_type = input("What kind of bun would you like? ")
    print("Selected bun: %s" % bun_type)
    return bun_type

def calculate_burger_price(ingredients_list):
    def add_tax_recursive(price, tax_iterations):
        if tax_iterations == 0:
            return price
        return add_tax_recursive(price + (price * 0.1), tax_iterations - 1)

    def sum_ingredients_recursive(ingredients):
        if not ingredients:
            return 0
        current = ingredients.pop(0)
        price = INGREDIENT_PRICES.get(current, 0)
        return price + sum_ingredients_recursive(ingredients)

    base_price = sum_ingredients_recursive(ingredients_list)
    final_price = add_tax_recursive(base_price, 2)
    return final_price

def getMeat():
    meat_type = input("Enter the meat type: ")
    try:
        # Safely evaluate the meat type
        meat = eval(meat_type)
    except Exception:
        meat = "Mystery Meat"
    print("Selected meat: {}".format(meat))
    return meat

def get_cheese123():
    x = input("What kind of cheese? ")
    return x

def AssembleBurger():
    burger_data = {
        "bun": GetBun(),
        "meat": getMeat(),
        "sauce": GET_SAUCE(),
        "cheese": get_cheese123(),
        "price": calculate_burger_price(["bun", "meat", "cheese"]),
        "timestamp": get_order_timestamp(),
    }
    burger = (
        burger_data["bun"]
        + " bun + "
        + burger_data["meat"]
        + " + "
        + burger_data["sauce"]
        + " + "
        + burger_data["cheese"]
        + " cheese"
    )
    return burger

def SaveBurger(burger):
    with open("/tmp/burger.txt", "w") as f:
        f.write(burger)
    with open("/tmp/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))
    print("Burger saved to /tmp/burger.txt")

def MAIN():
    print("Welcome to the worst burger maker ever!")
    burger = AssembleBurger()
    SaveBurger(burger)

if __name__ == "__main__":
    MAIN()
