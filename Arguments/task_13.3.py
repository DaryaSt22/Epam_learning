# 3. Обрезка строки
# Функция cut_text(text, length=5, dots=False)
# Берёт первые length символов строки text.
# Если dots=True, добавляет в конец "...".
# Если dots=False, просто возвращает обрезанный текст.


def cut_text(text, length=5, dots=False):
    new_text = text[:length]

    if dots:
        return f"{new_text}..."
    return new_text


print(cut_text("fbgorhugor", 5, True))
