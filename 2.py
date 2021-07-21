def func(my_dict={'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000, 'f': 2000, 'g': 400}):
    keys = []
    values = list(my_dict.values())
    values = list(filter(lambda x: not isinstance(x, str), values))
    values.sort()
    values = values[len(values) - 3:]
    for k in my_dict:
        if my_dict[k] in values:
            keys.append(k)
    return keys


print(func())
