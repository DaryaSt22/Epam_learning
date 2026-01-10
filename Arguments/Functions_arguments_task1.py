from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
    {'name': 'Roma', 'gender': 'male', 'sport': 'Sex-game'},
]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    pass


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    def fn(data):
        columns = ('name', 'gender', 'sport')

    return fn


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def fn(data: DataType) -> DataType:
        new_list = []

        for record in friends:
            for value in values:
                if record[column] == value:
                    new_list.append(record)

        return new_list
    return fn

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
