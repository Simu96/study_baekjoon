n = int(input())
number = list(map(int, input().split()))

array = [True] * 1001
# 0과 1은 소수가 아님
array[0] = False
array[1] = False

for i in range(2, 1001):
  if array[i] == True:
    j = 2
    while(i * j <= 1000):
      array[i * j] = False
      j += 1

cnt = 0

for i in range(n):
  if array[number[i]] == True:
    cnt += 1

print(cnt)
