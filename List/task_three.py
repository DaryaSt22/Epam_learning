from typing import List


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here

    result = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product = product * nums[j]
        result.append(product)

    return result

# print(foo([1, 2, 3]))


my_tuple = 40, 56.6, 90
print(my_tuple)
print(*my_tuple)