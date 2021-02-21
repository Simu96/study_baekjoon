import sys

n = int(sys.stdin.readline().rstrip())
m = [[0] * 3 for _ in range(n)]
sum = [[0] * 3 for _ in range(n)]

for i in range(n):
  m[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# 첫번째 비용을 저장
sum[0][0] = m[0][0]
sum[0][1] = m[0][1]
sum[0][2] = m[0][2]

# 2번째 부터 가능한 경우의 수를 sum에 저장(n이 1일 경우, index error)
for i in range(1, n):
  sum[i][0] = min(sum[i-1][1], sum[i-1][2]) + m[i][0]
  sum[i][1] = min(sum[i-1][0], sum[i-1][2]) + m[i][1]
  sum[i][2] = min(sum[i-1][0], sum[i-1][1]) + m[i][2]

# n번째에서 최소합 출력
print(min(sum[n-1]))
