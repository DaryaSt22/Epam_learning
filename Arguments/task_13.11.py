# 11. Обратная строка по флагу
# Функция normalize_string(text, strip_spaces=True, reverse=False)
# Если strip_spaces=True → убирает пробелы в начале и конце (.strip()).
# Если reverse=True → переворачивает строку.
# Можно применять оба флага одновременно.
# S.strip([chars])	Удаление пробельных символов в начале и в конце строки


def normalize_string(text, strip_spaces=True, reverse=False):
    if strip_spaces:
        text = text.strip()
    if reverse:
        text = text[::-1]

    return text


print(normalize_string("   Hello   "))
print(normalize_string("   Hello   ", strip_spaces=False))         
print(normalize_string("   Hello   ", strip_spaces=True, reverse=True))
print(normalize_string("   Hello   ", strip_spaces=False, reverse=True))
