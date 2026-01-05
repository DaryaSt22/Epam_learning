# 29. Ограниченный набор ключей
# Функция person_info(**kwargs):
# берёт из kwargs только ключи name, age, city,
# всё остальное игнорирует,
# возвращает новый словарь только с этими ключами (если их нет — не добавлять).

def person_info(**kwargs):
    new_dict = {}
    search_keys = ["name", "age", "city"]

    for key in search_keys:
        if key in kwargs:
            new_dict[key] = kwargs.get(key)

    return new_dict


print(person_info(name="Anna", age=254, city="Tallinn", hobby="Python"))
