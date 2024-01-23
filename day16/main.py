from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

end_order = False
while not end_order:
	order = input(f"What would you like? ({menu.get_items()}): ")
	if order == "off":
		end_order = True
	elif order == "report":
		coffeMaker.report()
		moneyMachine.report()
	elif menu.find_drink(order) is not None:
		coffee = menu.find_drink(order) 
		if coffeMaker.is_resource_sufficient(coffee):
			if moneyMachine.make_payment(coffee.cost):
				coffeMaker.make_coffee(coffee)
	