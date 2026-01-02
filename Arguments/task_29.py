# 29. Ограниченный набор ключей
# Функция person_info(**kwargs):
# берёт из kwargs только ключи name, age, city,
# всё остальное игнорирует,
# возвращает новый словарь только с этими ключами (если их нет — не добавлять).


def person_info(**kwargs):
    new_dict = {}

    if 'name' in kwargs:
        kwargs.get('name')
    elif 'age' in kwargs:
        kwargs.get('age')
    elif 'city' in kwargs:
        kwargs.get('city')

    return new_dict


print(person_info(name="Anna", age=25, city="Tallinn", hobby="Python"))
