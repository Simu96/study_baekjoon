import sys
from itertools import combinations

n = []
for i in range(9):
  n.append(int(sys.stdin.readline().rstrip()))

a = list(combinations(n, 7))
for i in range(len(a)):
  if sum(a[i]) == 100:
    b = sorted(a[i])
    break

for i in range(len(b)):
  print(b[i])
