import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)
d[1] = 1

if n > 1:
  d[2] = 3
  for x in range(3, n+1):
    d[x] = d[x-1] + d[x-2] * 2

print(d[n] % 10007)
