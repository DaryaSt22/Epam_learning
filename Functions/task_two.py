# Сделай отдельные выражения (без if, просто переменные), например:
# only_positive — True, если все числа в списке numbers больше 0.
# has_negative — True, если есть хотя бы одно отрицательное число в numbers.
# all_non_empty — True, если все строки в strings не пустые.
# has_empty — True, если хотя бы одна строка в strings пустая.
# Во всех четырёх случаях постарайся использовать только all или только any (и, возможно, сравнение типа x > 0).

numbers = [3, -1, 5, 10]
strings = ["cat", "", "dog"]

print(all(numbers))
print(all(strings))
print()

only_positive = all(n > 0 for n in numbers)
print(only_positive)
has_negative = any(n < 0 for n in numbers)
print(has_negative)
all_non_empty = all(st != '' for st in strings)
print(all_non_empty)
has_empty = any(st == '' for st in strings)
print(has_empty)