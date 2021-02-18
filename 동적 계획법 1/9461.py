import sys

t = int(sys.stdin.readline().rstrip())
p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1


for i in range(4, 101):
  p[i] = p[i-3] + p[i-2]  # 점화식


for j in range(t):
  n = int(sys.stdin.readline().rstrip())
  print(p[n])
