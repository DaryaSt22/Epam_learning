def filter_function(pair_item):
    return pair_item[1:2]

pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=filter_function)

print(filter_function([(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]))


pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=lambda pair_item: pair_item[1]) # Lambda returns pair_item[1]

print(filter_function([(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]))