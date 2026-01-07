# 34. Аргументы-конфиг
# Напиши функцию settings(**options), которая:
# принимает любые настройки,
# возвращает строку вида: "Settings: key1=value1; key2=value2; ...".
# Отсортируй ключи по алфавиту перед формированием строки (можно через sorted(options.items())).


def settings(**options):
    # print(options)
    sorted_dict_items = sorted(options.items(), key=lambda item: item[0])
    # return f"Setting: {sorted_dict_items}"
    parts = [f"{k}={v}" for k, v in sorted_dict_items]
    return "Settings: " + "; ".join(parts)


print(settings(theme="dark", lang="ru", debug=True))
