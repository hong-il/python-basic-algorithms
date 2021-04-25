f = open('/Users/bi/PycharmProjects/python-basic-algorithms/file.txt')
lines = f.readlines()
for line in lines:
    print(line, end="")