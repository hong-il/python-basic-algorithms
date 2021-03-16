import math

# 본 문제에서는 자연수 5개가 주어집니다.
#
# 숫자를 차례로 곱해 나온 수가 제곱수가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
# 코드를 작성해주세요.

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')
