"""Задача: есть список: [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
требуется получить строку: '  -3--1,2,10,15,16,18-20'
"""


def solution(args):
    result = []
    in_mind = None
    for element in range(len(args)):
        if element + 1 == len(args) or args[element] + 1 != args[element + 1]:
            if in_mind is not None and in_mind + 1 != args[element]:
                result.append(f'{in_mind}-{args[element]}')
                in_mind = None
            elif in_mind is not None and in_mind + 1 == args[element]:
                result.append(f'{in_mind},{args[element]}')
                in_mind = None
            else:
                result.append(str(args[element]))
        elif element + 1 == len(args) or args[element] + 1 == args[element + 1]:
            if in_mind is None:
                in_mind = args[element]  # -3
            else:
                continue
    return ','.join(result)


test = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
print(solution(test))

x = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
x = sorted(x)
x_max = max(x)
x_min = min(x)

y_range = list(range(x_min, x_max + 1))

used = []
answer = []
for num in x:
    temp_lst_num = []
    count = 0
    if num not in used:

        while True:
            num += count
            if num in x and num in y_range:
                temp_lst_num.append(num)
            else:
                answer.append(temp_lst_num)
                break

            used.append(num)
            count = 1
for index, num in enumerate(answer):
    if len(num) > 2:
        answer[index] = [f"{num[0]}-{num[-1]}"]
print(','.join(str(j) for i in answer for j in i))


def solution1(args):
    """зачетное решение"""
    result = []
    stored_element = None
    for element in range(len(args)):
        if element + 1 == len(args) or args[element] + 1 != args[element + 1]:
            if stored_element is not None:
                result.append(f'{stored_element}-{args[element]}')
                stored_element = None
            else:
                result.append(str(args[element]))
        elif stored_element is None:
            stored_element = args[element]
    return ','.join(result)

print('sol1')
print(solution1(test))


def sol2(data_list: list):
    data_list.sort(reverse=True)
    new_list, result_list, result = [], [], []

    for _ in range(len(data_list)):
        if len(data_list) >= 2 and data_list[-1] == data_list[-2] - 1:
            new_list.append(data_list.pop())
        else:
            new_list.append(data_list.pop())
            result_list.append(new_list.copy())
            new_list.clear()
    for item in result_list:
        element = f'{item[0]}-{item[-1]}' if len(item) > 2 else ','.join([str(elem) for elem in item])
        result.append(element)
    return ','.join(result)

print('sol2')
print(sol2(test))
