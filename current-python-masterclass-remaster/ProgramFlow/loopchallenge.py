# loopchallenge.py

menu = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
print("Please choose your option from the list below:")
for index in range(len(menu)):
		print("{}. {}".format(index, menu[index]))

choice = ""
while choice not in range(len(menu)):
	# choice = int(input("Make a choice from {} to {}: ".format(0, len(menu))))
	choice = int(input())
	while choice != 0:
		if choice not in range(len(menu)):
			for index in range(len(menu)):
				print("{}. {}".format(index, menu[index]))
			break
		else:
			print("You have chosen option {}".format(choice))
			# choice = int(input("Make a choice from {} to {}: ".format(0, len(menu))))
			choice = int(input())

# # solution 1

# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5:\tGo to bed")
# print("0:\tExit")

# while True:
	# choice = input()
	
	# if choice == "0":
		# break
	# elif choice in "12345":
		# print("You chose option {}".format(choice))
	# else:
		# print("Please choose your option from the list below:")
		# print("1:\tLearn Python")
		# print("2:\tLearn Java")
		# print("3:\tGo swimming")
		# print("4:\tHave dinner")
		# print("5:\tGo to bed")
		# print("0:\tExit")

# # solution 2

# choice = "-"
# while True:
	# if choice == "0":
		# break
	# elif choice in "12345":
		# print("You chose option {}".format(choice))
	# else:
		# print("Please choose your option from the list below:")
		# print("1:\tLearn Python")
		# print("2:\tLearn Java")
		# print("3:\tGo swimming")
		# print("4:\tHave dinner")
		# print("5:\tGo to bed")
		# print("0:\tExit")

	# choice = input()

# # solution 3

# choice = "-"
# while choice != "0":
	# if choice in "12345":
		# print("You chose option {}".format(choice))
	# else:
		# print("Please choose your option from the list below:")
		# print("1:\tLearn Python")
		# print("2:\tLearn Java")
		# print("3:\tGo swimming")
		# print("4:\tHave dinner")
		# print("5:\tGo to bed")
		# print("0:\tExit")

	# choice = input()