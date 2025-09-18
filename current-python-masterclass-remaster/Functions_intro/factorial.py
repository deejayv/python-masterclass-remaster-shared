# factorial.py


def factorial(number: int) -> int:
    """

    :param number:
    :return:
    """
    fact = 1
    if number != 0:
        for i in range(1, number + 1):
            fact *= i
        return fact
    else:
        return fact


n = input("Enter number of factorials to calculate: Press Enter to exit ")

while n != "":
    print()
    print("The first {} factorials are as follows: ".format(n))
    print()
    for i in range(int(n)):
        print("{} {}".format(i, factorial(i)))
    print()
    break
