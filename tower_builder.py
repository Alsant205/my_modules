def piramid_builder(n_floors):
    return [
        f'{" " * (n_floors - (star + 1))}' \
        f'{"*" * (star * 2 + 1)}' \
        f'{" " * (n_floors - (star + 1))}'
        for star in range(n_floors)
    ]


test = 3
# [ '   *   ',
#   '  ***  ',
#   ' ***** ',
#   '*******']  количество звезд = n * 2 - 1

print(piramid_builder(test))
