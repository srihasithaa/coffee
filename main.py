from data import MENU,resources
def report():
    water=int(resources["water"])
    milk=int(resources["milk"])
    coffee=int(resources["coffee"])
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")

def check_resources(flavour):
    water=resources["water"]
    milk=resources["milk"]
    coffee=resources["coffee"]

    if  flavour=="espresso":
        if water>=MENU[flavour]["ingredients"]["water"] and coffee>=MENU[flavour]["ingredients"]["coffee"]:
            return True
        return False
    else:
        if water>=MENU[flavour]["ingredients"]["water"] and coffee>=MENU[flavour]["ingredients"]["coffee"] and milk>=MENU[flavour]["ingredients"]["milk"]:
            return True
        return False

def process_coins(quarter,dime,nickel,penny):
    cost=(quarter*0.25)+(dime*0.1)+(nickel*0.05)+(penny*0.01)
    return round(cost,2)

def transaction(funds,flavour):
    cost=MENU[flavour]["cost"]
    if funds<cost:
        return -1
       
    elif funds>cost:
        return funds-cost
    
def modify_resources(flavour):
    resources["water"]-=float(MENU[flavour]["ingredients"]["water"])
    resources["milk"]-=float(MENU[flavour]["ingredients"]["milk"])
    resources["coffee"]-=float(MENU[flavour]["ingredients"]["coffee"])

def coffee():
    more_coffee=True
    while more_coffee:
        flavour=input("What would you like? (espresso/latte/cappuccino?").lower()

        if flavour=='report':
            report()

        elif check_resources(flavour):
            print("Please enter coins:")
            quarters=int(input("How many quarters? "))
            dimes=int(input("How many dimes? "))
            nickels=int(input("How many nickels? "))
            pennies=int(input("How many pennies? "))
            money=process_coins(quarters,dimes,nickels,pennies)

            proceed=transaction(money,flavour)
            if  proceed==-1:
                print("Sorry that's not enough money. Money refunded ")
            
            else:
                proceed=round(proceed,2)
                if proceed:
                    modify_resources(flavour)
                    print(f"Here is ${proceed} in change")
                    print(f"Here's your {flavour} Enjoy!")
                    # more_coffee=False
                    # break
        
        else: 
            print("Sorry! we do not enough ingredients! try another flavour!")

coffee()
