import collections
from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here

    s = s.lower()
    counter = collections.Counter(s)

    return counter


print(get_dict('Oh, it is python'))