# Counting sort 형태
import sys

n = int(input())

a = [0] * 10001

for i in range(n):
  b = int(sys.stdin.readline().strip())
  a[b] += 1

for i in range(10001):
  if a[i] != 0:
    for j in range(a[i]):
      print(i)
