# 27. Создание профиля из **kwargs
# Функция create_profile(**kwargs) пусть возвращает словарь kwargs без изменений.
# Потом вызови:
# create_profile(name="Anna", age=25)
# create_profile(city="Tallinn", hobby="Python")


def create_profile(**kwargs):
    return kwargs


print(create_profile(name="Anna", age=25))
print(create_profile(city="Tallinn", hobby="Python"))