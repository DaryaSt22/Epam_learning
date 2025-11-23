from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here

    pairs = list(zip(lst[0::1], lst[1::]))

    return pairs


print(get_pairs([1, 2, 3, 8, 9]))