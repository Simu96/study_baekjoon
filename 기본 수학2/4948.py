array = [True] * (123456 * 2 + 1)
# 0과 1은 소수가 아님
array[0] = False
array[1] = False

for i in range(2, 123456 * 2 + 1):
  if array[i] == True:
    j = 2
    while(i * j <= 123456 * 2):
      array[i * j] = False
      j += 1

n = 1

while(1):
  n = int(input())
  if n == 0:
    break
  cnt = 0
  for i in range(n + 1, 2 * n + 1):
    if array[i] == True:
      cnt += 1
  print(cnt)
