# 1. Повтор с разделителем и флагом
# Напиши функцию repeat_text(text, times=1, sep="", upper=False)
# Повторяет text times раз.
# Между повторами вставляет строку sep.
# Если upper=True, делает весь результат заглавными.
# Примеры вызова придумай сама.


def repeat_text(text, times=1, sep="", upper=False):
    if upper:
        text = text.upper()
    return sep.join([text] * times)


print(repeat_text("GHid", 2, "-", True))
print(repeat_text("GHid", 4, " ", False))
