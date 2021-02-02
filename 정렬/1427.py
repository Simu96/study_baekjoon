import sys

n = sys.stdin.readline().rstrip()
a = [0] * len(n)

for i in range(len(n)):
  a[i] = n[i]

a.sort(reverse=True)

for i in range(len(n)):
  print(a[i], end="")
