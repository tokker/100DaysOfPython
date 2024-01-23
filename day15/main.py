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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(coffee_type):
	for ingredient in MENU[coffee_type]["ingredients"]:
		if MENU[coffee_type]["ingredients"][ingredient] > resources[ingredient]:
			return ingredient
	return "ok"	
	
	
money = 0
end_order = False
while not end_order:
	customer_money = 0
	coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
	if coffee_type == "off":
		end_order = True
	elif coffee_type == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${money}")
	elif coffee_type not in MENU:
		print("There is no such coffee.")
	else:
		if check_resources(coffee_type) == "ok":
			print("Please insert coins.")
			customer_money += 0.25 * int(input("How many quarters?: "))
			customer_money += 0.1 * int(input("How many dimes?: "))
			customer_money += 0.05 * int(input("How many nickles?: "))
			customer_money += 0.01 * int(input("How many pennies?: "))
			if MENU[coffee_type]["cost"] > customer_money:
				print("Sorry that's not enough money. Money refunded.")
			else:
				print(f"Here is ${round(customer_money - MENU[coffee_type]['cost'], 2)} in change.")
				money = round(money + MENU[coffee_type]["cost"], 2)
				for ingredient in MENU[coffee_type]["ingredients"]:
					resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]
		else:
			print(f"Sorry there is not enough {check_resources(coffee_type)}.")
		