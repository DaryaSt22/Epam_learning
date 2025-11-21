from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    # TODO: Add your code here

    return sorted(list(set(str_list)))

if __name__ == "__main__":
    print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))