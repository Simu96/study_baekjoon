import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  arr.append((b, a))


arr.sort()

for i in range(n):
  print(arr[i][1], arr[i][0])
