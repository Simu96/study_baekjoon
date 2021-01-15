k = int(input())
for i in range(k):
  h, w, n = map(int, input().split())
  if n % h == 0:
    y = h
    x = int(n / h)
  else:
    y = int(n % h)
    x = int(n / h) + 1

  print(y, end="")
  print("%02d" %x)
