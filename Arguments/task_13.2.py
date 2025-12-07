# 2. Приветствие с формальным флагом
# Функция greet(name, formal=False)
# Если formal=False → возвращает строку вида: "Привет, {name}!"
# Если formal=True → "Здравствуйте, {name}."

def greet(name, formal=False):
    if formal == False:
        return f"Привет, {name}!"
    elif formal == True:
        return f"Здравствуйте, {name}."

print(greet("Katya", False))
print(greet("Kat", True))
