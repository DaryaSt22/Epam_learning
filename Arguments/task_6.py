# 6. Порядок аргументов
# Сделай функцию show_person(name, age, city) и вызови её:
# show_person("Anna", 25, "Tallinn")
# show_person(city="Tallinn", name="Anna", age=25)
# Пойми, почему оба вызова работают, и в чём отличие записи.


def show_person(name, age, city):
    print(name, age, city)

show_person("Anna", 25, "Tallinn")
show_person(city="Tallinn", name="Anna", age=25)




def generate_squares(**kwargs):
    return n ** n

print(generate_squares(5))



# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
