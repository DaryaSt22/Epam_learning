# Functions. Decorators. Final Task 2.
# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by indexes specified in indexes. Wrong indexes must be ignored. Examples:
#
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]


from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here
    """

    valid_indexes = set()

    for i in indexes:
        if 0 < i < len(s):
            valid_indexes.add(i)

    pts = [0] + sorted(valid_indexes) + [None]
    return [s[i:j] for i, j in zip(pts, pts[1:])]


print(split_by_index("pythoniscool,isn'tit?", [6, 6, 8, 8, 12, 13, 18, 18]))
print(split_by_index("no luck", [42]))
