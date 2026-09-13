import time
name = input('WHAT IS YOUR NAME?\n')
orderedtoppings = []
orderedprices = []
while 1==1:
    bal = int(input(f'\nOKAY {name}, HOW MUCH MONEY DO YOU WANT TO SPEND? (USD) [PLAIN PIZZA IS 5 USD]\n'))
    if bal < 5:
        print('\nINSUFFICIENT FUNDS, PLEASE CALL SOMEONE TO BRING YOU MONEY!\n')
        bal = int(input(f'OKAY {name}, HOW MUCH MONEY DO YOU WANT TO SPEND?\n'))
    while bal >= 5:
        print('\nTOPPINGS\n')
        toppings = ['NO TOPPINGS', 'EXTRA CHEESE', 'PARM', 'PEPPERONI', 'BACON', 'SAUSAGE']
        prices = [0, 1, 1, 3, 2, 3]
        counter = 0
        for i in range(len(toppings)):
            print(f'{counter + 1}. {(toppings[counter])} - {(prices[counter])} USD')
            counter += 1
        choice = int(input('\nWHAT TOPPING WOULD YOU LIKE TO ADD?\n'))
        while choice <= 0 or choice >= len(toppings) + 1:
            print(f'\nNUMBER {choice} IS NOT AN OPTION\n')
            counter = 0
            for i in range(len(toppings)):
                print(f'{counter + 1}. {(toppings[counter])} - {(prices[counter])} USD')
                counter += 1
            choice = int(input('\nWHAT TOPPING WOULD YOU LIKE TO ADD?\n'))
        print(f'YOU ADDED {(toppings[choice - 1])} FOR {(prices[choice - 1])} USD.')
        orderedtoppings.append(toppings[choice - 1])
        orderedprices.append(prices[choice - 1])
        total = sum(orderedprices) + 5
        if bal < total:
            orderedtoppings.remove(toppings[choice - 1])
            orderedprices.remove(prices[choice - 1])
            total = sum(orderedprices) + 5
            print('\nINSUFFICIENT FUNDS.')
            time.sleep(1)
        print(f'\nYOUR SHOPPING CART NOW ({total} USD TOTAL):\n')
        othercounter = 0
        for i in range(len(orderedtoppings)):
            print(f'{othercounter + 1}. {(orderedtoppings[othercounter])} - {(orderedprices[othercounter])} USD\n')
            total = sum(orderedprices) + 5
            othercounter += 1
        done = input(f'{name}, ARE YOU FINISHED WITH YOUR ORDER?\n')
        if done == 'yes':
            address = input(f'\n{name}, WHERE WOULD YOU LIKE THIS PIZZA SENT TO?\n')
            print('\nPIZZA ORDERED! IT WILL TAKE ABOUT 10 SECONDS TO DELIVER')
            time.sleep(1)
            print('\n10 (PIZZA PREP)')
            time.sleep(1)
            print('9 (ADDING TOPPINGS)')
            time.sleep(1)
            print('8')
            time.sleep(1)
            print('7 (BAKING THE PIZZA)')
            time.sleep(1)
            print('6')
            time.sleep(1)
            print('5 (BOXING THE PIZZA)')
            time.sleep(1)
            print('4 (DELIVERY BEGINS)')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print(f'1 (ARRIVED AT {address})')
            time.sleep(1)
            print(f'\nDELIVERY GUY: HERE YOU GO {name} ENJOY THIS PIZZA WITH {orderedtoppings}!')
            orderedtoppings = []
            orderedprices = []
            time.sleep(5)
            print('\n(ORDER ANOTHER PIZZA IN 10 SECONDS)\n')
            time.sleep(10)
            name = input('WHAT IS YOUR NAME?\n')
            bal = int(input(f'\nOKAY {name}, HOW MUCH MONEY DO YOU WANT TO SPEND? (USD)\n'))