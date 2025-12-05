# 3. Значения по умолчанию
# Создай функцию introduce(name, city="Tallinn"), которая печатает:
# "Меня зовут <name>, я живу в <city>".
# Проверь:
# вызов только с name;
# вызов с name и city.


def introduce(name, city="Tallinn"):
    return f"Меня зовут {name}, я живу в {city}"

print(introduce("Darya"))
print(introduce("Darya", "Vilnius"))