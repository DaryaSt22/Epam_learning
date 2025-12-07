# 13. Функция с флагом
# Напиши функцию repeat(text, times=1, upper=False).
# Если upper=True, делай текст заглавным.
# Проверь разные вызовы:
# repeat("hi")
# repeat("hi", 3)
# repeat("hi", upper=True)
# repeat("hi", times=3, upper=True)

def repeat(text, times=1, upper=False):
    if upper:
        text = text.upper()
    return text * times


print(repeat("hi", upper=True))
print(repeat("hi"))
print(repeat("hi", 3))
print(repeat("hi", times=3, upper=True))
