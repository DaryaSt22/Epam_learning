from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

# friends = [
#     {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
#     {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
#     {'name': 'Roma', 'gender': 'male', 'sport': 'Sex-game'},
#     {'name': 'Romfffa', 'gender': 'male', 'sport': 'Basketball'},
# ]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result = list(data)
    for f in filters:
        result = f(result)
    result = selector(result)
    return result


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    def fn(data: DataType) -> DataType:
        new_list = []
        for record in data:
            new_dict = {}
            for column in columns:
                if record.get(column) != None:
                    new_dict[column] = record.get(column)
            new_list.append(new_dict)
        return new_list

    return fn
# fa = select('gender')
# print(fa(friends))

def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def fn(data: DataType) -> DataType:
        new_list = []

        for record in data:
            for value in values:
                if record[column] == value:
                    new_list.append(record)

        return new_list
    return fn
# f = field_filter('gender', 'male')
# print(f(friends))

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
    # print(value)
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
