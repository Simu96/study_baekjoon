import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)
d[1] = 1

if n > 1:
  d[2] = 2

if n > 2:
  for x in range(3, n+1):
    d[x] = d[x-2] + d[x-1]

print(d[n] % 10007)
