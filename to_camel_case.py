def to_camel_case(text):
    """преобразует текст вида п_р или п-р в Кэмелкейс"""
    line, result = False, []

    for _ in range(len(text)):
        if text[_] == '_' or text[_] == '-':
            line = True
        elif line:
            result.append((text[_]).upper())
            line = False
        else:
            result.append(text[_])

    return ''.join(result)

test = "the_stealth_warrior"  # "theStealthWarrior"

print(to_camel_case(test))