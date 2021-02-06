"""
Указание Имен тех кто поставил лайк
"""


def likes_1(names):
    if len(names) == 0:
        return 'no one likes this'
    elif 0 < len(names) <= 3:
        if len(names) == 1:
            return names[0] + ' likes this'
        elif len(names) == 2:
            return names[0] + ' and ' + names[1] + ' like this'
        else:
            return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'


def likes_2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


# like_names = ['Alex']

like_names = ["Alex", "Dan", "Yliya", "Valentina"]


print(likes_2(like_names))
