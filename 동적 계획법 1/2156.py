import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)
sum = [0] * (n+1)
d[0] = 0

for i in range(1, n+1):
  d[i] = int(sys.stdin.readline().rstrip())

if n > 0:
  sum[1] = d[1]
if n > 1:
  sum[2] = sum[1] + d[2]

# i번째 포도주를 반드시 선택할 필요가 없다. 그러므로, i번째 포도주를 선택하는 경우와 i번째 포도주를 선택하지 않는 경우를 모두 고려해주어야 한다.(i번째 포도주를 선택하는 방법 : sum[i-3] + d[i-1] + d[i], sum[i-2] + d[i] 선택하지 않는 방법 : sum[i-1], sum[i-3] + d[i-1])
for i in range(3, n+1):
  sum[i] = max(sum[i-3] + d[i-1] + d[i], sum[i-2] + d[i], sum[i-1], sum[i-3] + d[i-1])

print(sum[n])
