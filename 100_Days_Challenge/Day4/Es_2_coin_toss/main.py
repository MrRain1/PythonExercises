from random import randint

print("Coin toss program.\nYou got:")
coin = randint(0, 1)

if coin:
    print("Heads")
else:
    print("Tails")