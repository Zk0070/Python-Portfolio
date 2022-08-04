print('Welcome to the Coffee Machine devloped by Zabi Khan!!')
print('***********************************')
print('''
  ___ ___  / _|/ _| ___  ___ 
  / __/ _ \| |_| |_ / _ \/ _ \  
 | (_| (_) |  _|  _|  __/  __/ 
  \___\___/|_| |_|  \___|\___| 
coffee bean - java - espresso - caffeine - brew - drink ''')
print('''

                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' met.
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------"" ''')
print('****************************************')
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
    "water": 1000,
    "milk": 1000,
    "coffee":1000,
}
profit=0
end_of_coffee=False
water_resource=resources['water']
milk_resource=resources['milk']
coffee_resource=resources['coffee']
resources['profit']=profit
money_generated=resources['profit']
while not end_of_coffee:
    coffee_choice=input('What would you like to have?(espresso/latte/cappuccino): ').lower()
    if coffee_choice=='report':
        print(f'You have only {water_resource} ml water left, {milk_resource}ml milk left, and {coffee_resource}ml coffee left! and money generated for the day is {profit}$')
        coffee_choice=input('What would you like to have?(espresso/latte/cappuccino): ').lower()
    if coffee_choice=='off':
        print('Thank you!!!turning off the machine for the day!!')
        break
    price=float(input('Enter the amount in money for latte :0.25$, for espresso:0.50$, for cappucino:1$,:$'))
    resources['price']=price
    money_generated=resources['price']
    if coffee_choice=='latte':
        change=price-0.25
        cost=0.25
        profit+=cost
        if price<0.25:
            print('Sorry sufficient money missing..Money refunded please try again..')
        elif water_resource>=200 and milk_resource>=150 and coffee_resource>=24:
            print(f'Here is your change!:{change}$')
            print('Here is your latte..Enjoy it!')
            water_resource=water_resource-200
            milk_resource=milk_resource-150
            coffee_resource=coffee_resource-24
        else:
            print('Sorry not enough resources for latte try a different coffee please!')
    elif coffee_choice=='espresso':
       change=price-0.50
       cost=0.50
       profit+=cost
       if price<0.50:
            print('Sorry sufficient money missing..Money refunded please try again..')
       elif water_resource>=50 and milk_resource>=10 and coffee_resource>=18 and price>=0.50:
          print(f'Here is your change!{change}$')
          print('Here is your espresso..Enjoy it')
          water_resource=water_resource-50
          milk_resource=milk_resource-10
          coffee_resource=coffee_resource-18
       else:
           print('Sorry not enough resources for espresso try a different coffee please!')
    elif coffee_choice=='cappucino':
       change=price-1
       cost=1
       profit+=cost
       if price<1:
           print('Sorry sufficient money missing..Money refunded please try again..')
       elif water_resource>=250 and milk_resource>=100 and coffee_resource>=24 and price>=1 :
           print(f'Here is your change!{change}$')
           print('Here is your cappucino..Enjoy it')
           water_resource=water_resource-250
           milk_resource=milk_resource-100
           coffee_resource=coffee_resource-24
       else:
        print('Sorry not enough resources to prepare the your selected coffee type for cappucino try a different coffee please!')
    
    
    




