list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list(map(lambda a, b: a + b, list1, list2))

# [7, 9, 11, 13, 15]
print(result)
