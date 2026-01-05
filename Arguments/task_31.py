# 31. Проверка наличия ключа
# Функция check_key(key, **kwargs) возвращает:
# True, если key есть в kwargs,
# False иначе.
# Примеры:
# check_key("age", age=20, name="Anna") → True
# check_key("city", age=20) → False


def check_key(key, **kwargs):

    if key in kwargs:
        return True
    else:
        return False


print(check_key("age", age=20, name="Anna"))
print(check_key("city", age=20))