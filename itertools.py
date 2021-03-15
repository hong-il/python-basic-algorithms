import itertools

my_list = [[1, 2], [3, 4]]

# 1
answer = sum(my_list, [])
# 2
list(itertools.chain.from_iterable(my_list))
# 3
list(itertools.chain(*my_list))
