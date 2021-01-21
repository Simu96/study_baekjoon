m = int(input())
n = int(input())

array = [True] * 10001
# 0과 1은 소수가 아님
array[0] = False
array[1] = False

for i in range(2, 10001):
  if array[i] == True:
    j = 2
    while(i * j <= 10000):
      array[i * j] = False
      j += 1

sum = 0
min = 0

for i in range(m, n + 1):
  if array[i] == True:
    sum += i
    if min == 0:
      min = i

if sum == 0:
  print("-1")
else:
  print(sum)
  print(min)
