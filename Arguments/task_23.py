# 23. Смешивание обычных аргументов и *args
# Напиши show_info(title, *details), где:
# title — обязательный первый аргумент,
# details — всё остальное.
# Потренируй: show_info("User", "Anna", 25, "Tallinn").

def show_info(title, *details):
    print(title)
    print(*details)

show_info("User", "Anna", 25, "Tallinn")