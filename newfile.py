'''THE PERFECT GUESS GAME'''
#Made By Laksh.Coder
#insta-id  : hackerlaksh22

import random

r = random.randint(1,10)

print("Alright Let's Started:")
g = input("Choose Any No. From 1 to 10: ")

if g == r:	
    	print("Wow You Won")
else:
    	print("Is Not that Easy Kid")

print("The Real Number Was" , r)
print("And You Chose" , g)


if g == r:	
    	print("Congrats")
else:
    	print("Try Again. Don't Give Up '")
