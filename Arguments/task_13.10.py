# 10. Проверка пароля
# Функция check_password(password, min_length=8, strict=False)
# Если strict=False → возвращает True, если длина пароля ≥ min_length.
# Если strict=True → дополнительно проверяет, что в пароле есть хотя бы одна цифра.
# (Можешь использовать цикл или оператор any() — сама выбери.)


def check_password(password, min_length=8, strict=False):
    if strict:
        password = any(ch.isdigit() for ch in password) and len(password) >= min_length
    if not strict:
        password = len(password) >= min_length
    return password

print(check_password("djgbbDDjj^&ljn2", 9, True))