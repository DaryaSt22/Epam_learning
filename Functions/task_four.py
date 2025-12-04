# Функция возвращает True, если в списке есть хотя бы одно отрицательное число.
# Используй any.

def has_negative(nums: list[int]) -> bool:
    return any(n < 0 for n in nums)

print(has_negative([1, 0, 55, 9, -5]))
