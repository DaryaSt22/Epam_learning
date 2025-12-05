# 2. Приветствие по имени
# Функция greet(name, greeting) должна печатать строку вида:
# "Привет, Катя!" или "Доброе утро, Катя!".
# Вызови функцию с разными комбинациями позиционных и именованных аргументов.

def greet(name, greeting):
    result = f"{greeting}, {name}!"
    return result


print(greet("Катя", "Привет"))
print(greet(greeting="Доброе утро", name="Катя"))
