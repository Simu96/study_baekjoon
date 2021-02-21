# 1149.py와 비슷한 풀이
import sys

n = int(sys.stdin.readline().rstrip())
m = []
sum = []  # 경로의 max값을 저장할 배열

for i in range(n):
  m.append(list(map(int, sys.stdin.readline().rstrip().split())))

sum = m  # m으로 초기화

for i in range(1, n):
  for j in range(i+1):
    if j == 0:  # 가장 왼쪽 경로
      sum[i][j] = sum[i-1][j] + m[i][j]
    elif j == i:  # 가장 오른쪽 경로
      sum[i][j] = sum[i-1][j-1] + m[i][j]
    else: # 그 외 경로의 최대값은 [i-1][j-1]와 [i-1][j]사이중 최댓값에 현재 [i][j]의 값을 더한 값이다.
      sum[i][j] = max(sum[i-1][j-1], sum[i-1][j]) + m[i][j]

print(max(sum[n-1]))
