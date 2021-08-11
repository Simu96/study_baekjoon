import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * 1000001
d[0] = 1
d[1] = 2
d[2] = 4

# 최대 d[y]까지 미리 계산해야 메모리 초과를 방지할 수 있다.(m에 대하여 매번 갱신하면 메모리 초과를 야기함)
for y in range(3, 1000001):
    d[y] = (d[y-3] + d[y-2] + d[y-1]) % 1000000009

for x in range(n):
  m = int(sys.stdin.readline().rstrip())
  print(d[m-1])
