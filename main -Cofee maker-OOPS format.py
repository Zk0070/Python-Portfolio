from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
is_on=True

while is_on:
  choice=input('What would you like to have (latte/espresso/cappuchino): ')
  if choice=='off':
    print('Thank you machine is turning off for the day')
    is_on=False
  elif choice=='report':
    coffee_maker.report()
    money_machine.report()
  else:
    drink=menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
  
  
