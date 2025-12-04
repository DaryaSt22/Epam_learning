# Вернуть True, если все строки в списке имеют длину больше 3, иначе False

def all_long(strings: list[str]) -> bool:
    return all(len(st) > 3 for st in strings)

print(all_long(["cat", "djngr", "hohoh", "Bah", "Ball"]))