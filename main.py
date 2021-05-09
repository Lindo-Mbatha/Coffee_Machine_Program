from menu import MENU
from menu import resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

water_value = int(water)
milk_value = int(milk)
coffee_value = int(coffee)

money = 0

o = " "

x = True

while x is True:
    print(o)
    answer = input("What would like? espresso or latte or cappuccino? ").lower()

    if answer == "espresso":
        if water_value < 50:
            print(o)
            print("Sorry there is not enough water.")
        elif coffee_value < 18:
            print(o)
            print("Sorry there is not enough coffee.")
        elif water_value >= 50 and coffee_value >= 18:
            print(o)
            print("Please insert coins")
            answer_coins1 = input("How many (0.25) quarters? ")
            answer_coins2 = input("How many (0.10) dimes? ")
            answer_coins3 = input("How many (0.05) nickles? ")
            answer_coins4 = input("How many (0.1) pennies? ")

            total_q = float(answer_coins1) * 0.25
            total_d = float(answer_coins1) * 0.10
            total_n = float(answer_coins1) * 0.05
            total_p = float(answer_coins1) * 0.01

            total_coins = total_q + total_d + total_n + total_p

            if total_coins < 1.5:
                print(o)
                print("Not enough money, here is your money back. Please try again.")

            elif total_coins >= 1.5:
                for key in MENU:
                    if key == "espresso":
                        water_c = MENU[key]["ingredients"]["water"]
                        water_value = water_value - int(water_c)
                        coffee_c = MENU[key]["ingredients"]["coffee"]
                        coffee_value = coffee_value - int(coffee_c)
                        cost_e = (MENU[key]["cost"])

                money = money + 1.5

                total = total_coins - cost_e

                total2 = ("{:.2f}".format(total))

                print(o)
                print(f"Here is ${total2} in change.")
                print("Here is your espresso ☕.")

    elif answer == "latte":
        if water_value < 200:
            print(o)
            print("Sorry there is not enough water.")
        elif milk_value < 150:
            print(o)
            print("Sorry there is not enough milk.")
        elif coffee_value < 24:
            print(o)
            print("Sorry there is not enough coffee.")
        elif water_value >= 200 and milk_value >= 150 and coffee_value >= 24:
            print(o)
            print("Please insert coins")
            answer_coins1 = input("How many (0.25) quarters? ")
            answer_coins2 = input("How many (0.10) dimes? ")
            answer_coins3 = input("How many (0.05) nickles? ")
            answer_coins4 = input("How many (0.1) pennies? ")

            total_q = float(answer_coins1) * 0.25
            total_d = float(answer_coins1) * 0.10
            total_n = float(answer_coins1) * 0.05
            total_p = float(answer_coins1) * 0.01

            total_coins = total_q + total_d + total_n + total_p

            if total_coins < 2.5:
                print(o)
                print("Not enough money, here is your money back. Please try again.")

            elif total_coins >= 2.5:

                for key in MENU:
                    if key == "latte":
                        water_c = MENU[key]["ingredients"]["water"]
                        water_value = water_value - int(water_c)
                        milk_c = MENU[key]["ingredients"]["milk"]
                        milk_value = milk_value - int(milk_c)
                        coffee_c = MENU[key]["ingredients"]["coffee"]
                        coffee_value = coffee_value - int(coffee_c)
                        cost_e = (MENU[key]["cost"])

                money = money + 2.5

                total = total_coins - cost_e

                total2 = ("{:.2f}".format(total))

                print(o)
                print(f"Here is ${total2} in change.")
                print("Here is your latte ☕.")

    elif answer == "cappuccino":
        if water_value < 250:
            print(o)
            print("Sorry there is not enough water.")
        elif milk_value < 100:
            print(o)
            print("Sorry there is not enough milk.")
        elif coffee_value < 24:
            print(o)
            print("Sorry there is not enough coffee.")
        elif water_value >= 250 and milk_value >= 100 and coffee_value >= 24:
            print(o)
            print("Please insert coins")
            answer_coins1 = input("How many (0.25) quarters? ")
            answer_coins2 = input("How many (0.10) dimes? ")
            answer_coins3 = input("How many (0.05) nickles? ")
            answer_coins4 = input("How many (0.1) pennies? ")

            total_q = float(answer_coins1) * 0.25
            total_d = float(answer_coins1) * 0.10
            total_n = float(answer_coins1) * 0.05
            total_p = float(answer_coins1) * 0.01

            total_coins = total_q + total_d + total_n + total_p

            if total_coins < 3.0:
                print(o)
                print("Not enough money, here is your money back. Please try again.")

            elif total_coins >= 3.0:
                for key in MENU:
                    if key == "cappuccino":
                        water_c = MENU[key]["ingredients"]["water"]
                        water_value = water_value - int(water_c)
                        milk_c = MENU[key]["ingredients"]["milk"]
                        milk_value = milk_value - int(milk_c)
                        coffee_c = MENU[key]["ingredients"]["coffee"]
                        coffee_value = coffee_value - int(coffee_c)
                        cost_e = (MENU[key]["cost"])

            money = money + 3.0

            total = total_coins - cost_e

            total2 = ("{:.2f}".format(total))

            print(o)
            print(f"Here is ${total2} in change.")
            print("Here is your cappuccino ☕.")

    elif answer == "report":
        print(o)
        print(f"Water: {water_value}ml")
        print(f"Milk: {milk_value}ml")
        print(f"Coffee: {coffee_value}g")
        print(f"Money: ${money}")
