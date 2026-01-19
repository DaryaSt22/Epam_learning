# 42. Функция с разными типами аргументов
# format_message(user, /, text, *args, prefix="[MSG]", **kwargs)
# Придумай реалистичное поведение, где:
# user всегда позиционный,
# есть доп. позиционные (*args),
# есть именованные настройки (**kwargs, например uppercase=True).


def format_message(user, /, text, *args, prefix="[MSG]", **kwargs):
    pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
    pairs.sort()
    return pairs, user, text, args, prefix, kwargs


print(format_message("All", "lolo", 125, 44, cake="Lemon"))