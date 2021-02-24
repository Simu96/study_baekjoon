import sys

n = int(sys.stdin.readline().rstrip())

d = [[0 for _ in range(10)] for _ in range(n+1)]


d[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if n > 0: # 런타임 오류 방지(index error)
  d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 1자리 수의 경우 0이 올 수 없다.

for i in range(2, n+1):
  for j in range(10):
    if j == 0:  # 앞자리가 0인 경우 1만 올 수 있으므로 i-1자릿수의 1의 경우만 올 수 있다.
      d[i][j] = d[i-1][1]
    elif j == 9:  # 앞자리가 9인 경우 8만 올 수 있으므로 i-1자릿수의 1의 경우만 올 수 있다.
      d[i][j] = d[i-1][8]
    else: # 앞자리가 1~8인 경우 -1, +1 인 수가 올 수 있으므로 두가지 경우를 더해준다.
      d[i][j] = d[i-1][j-1] + d[i-1][j+1]


print(sum(d[n]) % 1000000000)
