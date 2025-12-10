# 17. Конкатенация строк
# Функция concat_strings(*parts) должна соединять все части в одну строку через пробел.
# Например: concat_strings("Hello", "my", "friend") → "Hello my friend".


def concat_strings(*parts):
    result_with_space = " ".join(parts)
    return result_with_space


print(concat_strings("Hello", "my", "friend"))
