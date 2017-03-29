import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("Starting price ${:,.2f}".format(price))

day = 0
while price >= MIN_PRICE and price <= MAX_PRICE: #not end of program
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1: #1 == 50% chance increase while 2 == 50% chance decrease(this is purely random)
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
        #print("I",price_change)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
        #print("D",price_change)

    price *= (1 + price_change)
    print("On day {} price is ${:,.2f}".format(day, price))


#for index, value in enumerate(my_str4):
