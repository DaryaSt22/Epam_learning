# Define a function linear_seq(sequence) which converts a passed sequence to a sequence without nested sequences.
# Example:
# def linear_seq(sequence):
#     pass
# sequence = [1,2,3,[4,5, (6,7)]]
# >>> print(linear_seq(sequence))
# [1,2,3,4,5,6,7]

from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here
    """
    result = []
    for x in sequence:
        if not isinstance(x, (list, tuple)):
            result.append(x)
        elif isinstance(x, (list, tuple)):
            for item in x:
                if isinstance(item, (list, tuple)):
                    result.extend((item))
                else:
                    result.append(item)

    return result