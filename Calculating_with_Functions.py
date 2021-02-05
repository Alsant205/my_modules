def zero(arg=''):
    return 0 if arg == '' else action(0, arg)


def one(arg=''):
    return 1 if arg == '' else action(1, arg)


def two(arg=''):
    return 2 if arg == '' else action(2, arg)


def three(arg=''):
    return 3 if arg == '' else action(3, arg)


def four(arg=''):
    return 4 if arg == '' else action(4, arg)


def five(arg=''):
    return 5 if arg == '' else action(5, arg)


def six(arg=''):
    return 6 if arg == '' else action(6, arg)


def seven(arg=''):
    return 7 if arg == '' else action(7, arg)


def eight(arg=''):
    return 8 if arg == '' else action(8, arg)


def nine(arg=''):
    return 9 if arg == '' else action(9, arg)


def action(digit, arg):
    if list(arg)[0] == '+':
        return digit + int(list(arg)[-1])
    elif list(arg)[0] == '-':
        return digit - int(list(arg)[-1])
    elif list(arg)[0] == '/':
        return int(digit / int(list(arg)[-1]))
    elif list(arg)[0] == '*':
        return digit * int(list(arg)[-1])


def plus(arg):
    return f'+{arg}'


def minus(arg):
    return f'-{arg}'


def times(arg):
    return f'*{arg}'


def divided_by(arg):
    return f'/{arg}'


print(one(divided_by(nine())))

# four(plus(nine())) # must return 13
