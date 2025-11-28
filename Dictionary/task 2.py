def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    """
    Add your code here or call it from here
    """

    new_list = []

    for i in range(row_start, row_end + 1):
        row = []
        for j in range(column_start, column_end + 1):
            row.append(i * j)

        new_list.append(row)


print(check(2,4,3,7))