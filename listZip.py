myList = [[1, 2, 3], [4, 5, 6]]
new_list = list(map(list, zip(*myList)))
# [[1, 4], [2, 5], [3, 6]]
print(new_list)
