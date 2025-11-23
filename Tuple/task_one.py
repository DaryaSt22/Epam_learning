from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here

    num_list = list(str(num))
    num_list_tuple = tuple(map(int, num_list))

    return num_list_tuple


print(get_tuple(87178291199))