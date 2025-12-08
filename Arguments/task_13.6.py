# 6. Смайлики по флагам
# Функция make_message(text, happy=True, loud=False)
# Если happy=True, добавляет в конец строки " :)", если False — " :(".
# Если loud=True, делает весь текст заглавным.
# Порядок: сначала работай с регистром, потом добавляй смайлик.


def make_message(text, happy=True, loud=False):
    new_text = text
    if loud:
        new_text = new_text.upper()
    if happy:
        new_text = new_text + " :)"
    else:
        new_text = new_text + " :("
    return new_text

print(make_message("Hello, Dolly!", False, True))
print(make_message("Hello, Dolly!", True, False))
print(make_message("Hello, Dollysdd!"))
