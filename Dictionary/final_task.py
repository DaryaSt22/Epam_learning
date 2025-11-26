from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here
    """

    unique_values = []

    for d in lst:
        # d.values()
        unique_values.extend(d.values())

    return set(unique_values)


print(check(
    [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]))
