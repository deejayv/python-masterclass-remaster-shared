# the_magical_adder.py

values = input("Please enter three numbers, separated by commas")

values_list = values.split(",")

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

magical_adder = values_list[0] + values_list[1] - values_list[2]
print(magical_adder)
