# 11. Преобразование температуры
# Функция convert(temp, unit_from, unit_to="C") — пока просто печатает аргументы.
# Сделай несколько вызовов функции с разными комбинациями обычных и именованных аргументов.

def convert(temp, unit_from, unit_to="C"):
    print(temp, unit_from, unit_to)

convert(2, 8, "9")
convert(unit_to="10", temp=4, unit_from=6)
convert(15, unit_from=6, unit_to="44")
