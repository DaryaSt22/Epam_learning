# 30. Значение по умолчанию через kwargs.get
# Та же функция person_info пусть:
# если city нет в kwargs, подставляет "Unknown".
# (Используй kwargs.get("city", "Unknown").)


def person_info(**kwargs):
    new_dict = {}
    search_keys = ["name", "age", "city"]

    for key in search_keys:
        if key in kwargs:
            new_dict[key] = kwargs.get(key)
        #if not "city" in kwargs:
            #new_dict[key] = kwargs.get(key, "Unknown")

    new_dict["city"] = kwargs.get("city", "Unknown")

    return new_dict


print(person_info(name="Anna", age=2524, hobby="Python"))
