# Вернуть True, если в списке words есть хотя бы одно слово "python" (в точности такое).
# Используй any.


def contains_python(words: list[str]) -> bool:
    return any(wor == "python" for wor in words)

print(contains_python(["cat", "djngr", "hohoh", "Bah", "Ball", "python"]))
