m, n = map(int, input().split())

array = [True] * 1000001
# 0과 1은 소수가 아님
array[0] = False
array[1] = False

for i in range(2, 1000001):
  if array[i] == True:
    j = 2
    while(i * j <= 1000000):
      array[i * j] = False
      j += 1

for i in range(m, n + 1):
  if array[i] == True:
    print(i)
