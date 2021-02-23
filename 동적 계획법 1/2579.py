import sys

n = int(sys.stdin.readline().rstrip())
m = [0] * n
sum = [0] * n # 경로 최댓값을 저장할 배열

for i in range(n):
  m[i] = int(sys.stdin.readline().rstrip())


sum[0] = m[0]
if n > 1: # 런타임 에러 방지(index error)
  sum[1] = m[0] + m[1]
if n > 2:
  sum[2] = max(m[0] + m[2], m[1] + m[2])

# 4번째부터 점화식 적용(예시 : 4번째 계단에서 최댓값은 (1번째 계단까지의 최댓값 + 3번째 계단의 값 + 현재 계단의 값), (2번째 계단까지의 최댓값 + 현재 계단의 값)중 더 큰 값이다.)
for i in range(3, n):
  sum[i] = max(sum[i-3] + m[i-1] + m[i], sum[i-2] + m[i])

print(sum[n-1])
