# 5. Список в строку
# Функция list_to_string(items, sep=", ", reverse=False)
# Соединяет элементы списка items в строку через разделитель sep.
# Если reverse=True → сначала разворачивает список, потом соединяет.


def list_to_string(items, sep=", ", reverse=False):
    items = sep.join(items)
    if reverse:
        items = reversed(items)


    return items


print(list_to_string(["Cat", "1456", "22", "88", "3648", "Dog", "Milk"], ";", True))
