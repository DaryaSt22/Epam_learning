# 14. Аргументы в неправильном порядке
# Напиши функцию profile(name, age, country)
# Попробуй мысленно вызвать: profile(25, "Anna", "Estonia").
# Опиши, почему это формально корректно, но логически неверно.

def profile(name, age, country):
    print(name, age,country)

print(25, "Anna", "Estonia")