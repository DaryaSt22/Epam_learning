# 8. Фильтр коротких слов
# Функция filter_words(words, max_len=3, keep_short=True)
# Если keep_short=True → возвращает список слов, длина которых ≤ max_len.
# Если keep_short=False → наоборот, возвращает только слова, длина которых > max_len.


def filter_words(words, max_len=3, keep_short=True):
    result = []
    for word in words:
        if keep_short == True and len(word) <= max_len:
            result.append(word)
        if keep_short == False and len(word) > max_len:
            result.append(word)

    return result


print(filter_words(["Doloto", "Maska", "Cream", "Cat"], 5, False))
