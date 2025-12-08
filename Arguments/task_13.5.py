# 5. Список в строку
# Функция list_to_string(items, sep=", ", reverse=False)
# Соединяет элементы списка items в строку через разделитель sep.
# Если reverse=True → сначала разворачивает список, потом соединяет.


def list_to_string(items, sep=", ", reverse=False):
    # items = sep.join(items)
    if reverse:
        items = sep.join(map(str, reversed(items)))
    else:
        return sep.join(items)

    return items


print(list_to_string(["Cat", "1456", "22", "88", "3648", "Dog", "Milk"], ", ", True))




# def list_to_string(items, sep=", ", reverse=False):
#     # если нужно развернуть список — разворачиваем его
#     if reverse:
#         items = list(reversed(items))   # или items = items[::-1]
#
#     # на этом этапе items уже в нужном порядке
#     # приводим все элементы к строкам
#     str_items = map(str, items)
#
#     # соединяем строки через разделитель sep и возвращаем результат
#     return sep.join(str_items)
