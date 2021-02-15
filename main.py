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
