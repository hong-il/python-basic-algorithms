from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 6, 8]
x = 4
y = 8

# 2
# 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 5
# 6
print(bisect_left(a, y))
print(bisect_right(a, y))
