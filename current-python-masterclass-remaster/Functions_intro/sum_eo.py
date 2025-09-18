# sum_eo.py


def sum_eo(n,t):
    number = 0
    if t == "e":
        for i in range(n):
            if i % 2 == 0:
                number += i
        return number
    elif t == "o":
        for i in range(n):
            if i % 2 != 0:
                number += i
        return number
    else:
        return -1


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
