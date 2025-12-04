# Напиши функцию и она должна возвращать True, если все числа в списке nums чётные, иначе False.
# Используй all.



def all_even(nums: list[int]) -> bool:
    return all(n % 2 == 0 for n in nums )

print(all_even([1, 5, 6, -7, 555]))