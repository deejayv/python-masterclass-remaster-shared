# ifchallenge.py

name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
	print("Welcome to the holiday, {}".format(name))
else:
	print("Sorry, no holiday for you")