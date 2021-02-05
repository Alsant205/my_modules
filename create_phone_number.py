def create_phone_number(array):
    result = ['(']
    for element in array:
        result.append(str(element))
        result.append(') ') if len(result) == 4 else result.append('-') if len(result) == 8 else None
    return ''.join(result)


def create_phone_number_1(array):
    a = ''.join(str(element) for element in array)  # преобразование в строки и объединение в строку
    return f'({a[0:3]}) {a[3:6]}-{a[6:10]}'


test = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]  # "(023) 056-0890"

print(create_phone_number(test))
print(create_phone_number_1(test))
