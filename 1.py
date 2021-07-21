MIN = 8
MAX = 8 * 5


def func(a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
    b = []
    for i in a:
        if MIN < i < MAX:
            b.append(i)
    return b


print(func())
print(func([5, 38, 10, 6, 99]))