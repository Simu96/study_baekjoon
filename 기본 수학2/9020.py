t = int(input())
array = [True] * (10001)
array[0] = False
array[1] = False

for i in range(2, 10001):
  j = 2
  if array[i] == True:
    while(i * j <= 10000):
      array[i * j] = False
      j += 1

for i in range(t):
  n = int(input())
  
  a = 0
  b = 0

  for i in range(2, n + 1):
    if array[i] == True and array[n-i] == True and i <= n - i:
      a = i
      b = n - i
  print(a, b)
  
