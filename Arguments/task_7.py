# 7. Функция с одним аргументом по умолчанию
# Функция power(base, exp=2) — возвращает base ** exp.
# Протестируй:
# power(3)
# power(3, 3)
# power(base=2, exp=5)
# power(exp=5, base=2)


def power(base, exp=2) -> int:
    return base ** exp

print(power(3))
print(power(3, 3))
print(power(base=2, exp=5))
print(power(exp=5, base=2))