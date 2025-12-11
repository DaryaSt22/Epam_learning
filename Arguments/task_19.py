# 19. Сколько аргументов пришло?
# Функция count_args(*args) должна возвращать количество переданных аргументов.
# Примеры:
# count_args(1, 2, 3) → 3
# count_args() → 0

def count_args(*args):
    return len(args)

print(count_args(1, 2, 3))
print(count_args())