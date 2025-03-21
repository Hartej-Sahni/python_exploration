MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO 1: Print report
def print_report():
    print(f"water: {resources['water']} ml")
    print(f"milk: {resources['milk']} ml")
    print(f"coffee: {resources['coffee']} g")
    print(f"profit: ${profit}")


#TODO 2: Check resources sufficient?
def check_resources(type_of_coffee):
    water_required = MENU[type_of_coffee]["ingredients"]["water"] if "water" in MENU[type_of_coffee]["ingredients"] else 0
    milk_required = MENU[type_of_coffee]["ingredients"]["milk"] if "milk" in MENU[type_of_coffee]["ingredients"] else 0
    coffee_required = MENU[type_of_coffee]["ingredients"]["coffee"] if "coffee" in MENU[type_of_coffee]["ingredients"] else 0
    print(f"{water_required}  {milk_required}  {coffee_required}")
    print(f"{resources['water']}  {resources['milk']}  {resources['coffee']}")
    if (resources["water"] < water_required):
        return "Sorry, not enough water"
    if (resources["milk"] < milk_required):
        return "Sorry, not enough milk"
    if (resources["coffee"] < coffee_required):
        return "Sorry, not enough coffee"
    resources["water"] -= water_required
    resources["milk"] -= milk_required
    resources["coffee"] -= coffee_required
    global profit
    profit += MENU[type_of_coffee]["cost"]
    return f"Here is your {type_of_coffee}. Enjoy!"


#TODO 3: Process coins
def process_coins(quarters, dimes, nickels, pennies):
    total_pay = round((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01), 2)
    return total_pay


#TODO 4: Check transaction successful?
def check_transaction(type_of_coffee, amount_paid):
    if (amount_paid >= MENU[type_of_coffee]["cost"]):
        return True
    return False


#TODO 5: Make coffee
coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
while (coffee != "off"):
    if (coffee == "report"):
        print_report()
    elif (coffee == "espresso" or coffee == "latte" or coffee == "cappuccino"):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        amount_paid = process_coins(quarters, dimes, nickels, pennies)
        if (check_transaction(coffee, amount_paid)):
            change = round(amount_paid - MENU[coffee]["cost"], 2)
            if (change != 0):
                print(f"Here is ${change} in change.")
            print(check_resources(coffee))
        else:
            print("Sorry, that's not enough money. Money refunded.")
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
