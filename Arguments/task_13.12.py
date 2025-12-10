# 12. Логирование действий
# Функция process_number(n, square=False, cube=False, debug=False)
# Если square=True → вместо n берётся n**2.
# Если cube=True → вместо n берётся n**3.
# (Если оба True — выбери сама, что делать, и опиши это в комментарии.)
# Если debug=True → функция должна возвращать строку вида
# "Исходное: {старое_значение}, результат: {новое_значение}"
# Если debug=False → возвращает просто число.


def process_number(n, square=False, cube=False, debug=False):
    old_n = n
    if square:
        n = n ** 2
    elif cube:
        n_cube = n ** 3
    elif square and cube:
        n_four = n ** 4
    elif debug:
        debug_string = f"Исходное: {old_n}, результат: {n}"
  

    return n

