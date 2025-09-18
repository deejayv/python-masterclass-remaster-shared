# strings2.py

# #         012345678901234
# parrot = "Norwegian Blue"
# #         43210987654321  for negative indexing

# print(parrot[0:6:2])    # Nre
# print(parrot[0:6:3])    # Nw

number = input("Please enter a series of numbers, using any separators you like: ")
# separators = number[1::4]
separators = ""

for char in number:
	if not char.isnumeric():
		separators = separators + char
		
print(separators)
# print(type(separators))

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
