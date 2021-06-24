import sys
import math

t = int(sys.stdin.readline().rstrip())
m = [0] * t
n = [[] for _ in range(t)]

for i in range(t):
  m[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(t):
  for j in range(1, len(m[i])):
    for k in range(j+1, len(m[i])):
      x = math.gcd(m[i][j], m[i][k])
      n[i].append(x)

for i in range(t):
  print(sum(n[i]))
