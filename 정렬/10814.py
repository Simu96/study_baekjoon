import sys

n = int(sys.stdin.readline().rstrip())
data = []

for i in range(n):
  (a, b) = sys.stdin.readline().rstrip().split()
  # 나이는 int형으로 변환해주어야 오답으로 인식 안함
  a = int(a)
  data.append((a, b))

# 첫번째 튜플을 기준으로 정렬(reverse 가능)
data.sort(key = lambda x: x[0])

for i in range(n):
  print(data[i][0], data[i][1])
