# List
a = [i for i in range(20) if i % 2 == 1]
# result : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(a)
# same result
a = []
for i in range(20):
    if i % 2 == 1:
        a.append(i)
print(a)
# Two dimension list
n = 4
m = 3
array = [[0] * m for _ in range(n)]
# result : [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(array)
# List's functions
# result : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
a.append(21)
# result : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
a.sort()
# result : [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
a.sort(reverse=1)
# result : [21, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
a.insert(1, 21)
# result : 2
a.count(21)
# result : [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
a.remove(21)
