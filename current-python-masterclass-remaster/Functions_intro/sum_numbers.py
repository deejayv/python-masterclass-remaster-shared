# sum_numbers.py


def sum_numbers(*val: float) -> float:
    """
    Takes an n number of values and adds them up.
    :param val: The values to add.
    :return: The sum of all values.
    """
    total = 0
    for item in val:
        total += item
    return total


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
