num = '444'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * (base ** idx)

print(answer)
