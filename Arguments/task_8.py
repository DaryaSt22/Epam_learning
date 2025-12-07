# 8. Несколько значений по умолчанию
# Функция make_full_name(first, last, middle="") возвращает строку полного имени.
# Если middle == "", не добавляй отчество.
# Потренируйся вызывать:
# с двумя аргументами,
# с тремя,
# с именованными аргументами в другом порядке.

def make_full_name(first, last, middle="") -> str:
    if middle == "":
        return f"{first} {last}"
    else:
        return f"{first} {last} {middle}"

print(make_full_name("Dasha", "Stath", "GOG"))
print(make_full_name(last="ST", middle="Lot", first="DAR"))
print(make_full_name("Dasha", "Stath", ""))