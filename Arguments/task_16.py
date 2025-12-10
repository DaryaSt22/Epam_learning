# 16. Сумма произвольного количества чисел
# Напиши функцию sum_all(*numbers), которая возвращает сумму всех переданных чисел.
# Проверь вызовы:
# sum_all(1, 2, 3)
# sum_all()
# sum_all(10, -5, 7, 3)

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(10, 5, 9, 6, 4))
print(sum_all(1, 2, 3))
print(sum_all())
print(sum_all(10, -5, 7, 3))