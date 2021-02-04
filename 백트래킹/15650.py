import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
  a.append(i + 1)

# 조합 리스트
result = list(combinations(a, m))

# 리스트 길이만큼
for i in range(len(result)):
  # 리스트 원소의 길이만큼
  for j in range(len(result[i])):
    print(result[i][j], end = " ")
  print("")
