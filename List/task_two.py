from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here

    numbers = range(int(input()))
    my_list = list(numbers)

    if n % 3 == 0:
        my_list.append("Fizz")
    elif n % 5 == 0:
        my_list.append("Buzz")
    elif n % 3 == 0 and n % 5 == 0:
        my_list.append("FizzBuzz")

    return my_list


print(get_fizzbuzz_list(n=10))



from typing import Union, List

ListType = List[Union[int, str]]

def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here

    my_list = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            my_list.append("FizzBuzz")
        elif i % 3 == 0:
            my_list.append("Fizz")
        elif i % 5 == 0:
            my_list.append("Buzz")
        else:
            my_list.append(i)

    return my_list

print(get_fizzbuzz_list(n=35))