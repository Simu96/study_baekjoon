n, m = map(int, input().split())
min = 64
array = [[0] * m for _ in range(n)]
version_A = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B','W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

version_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

for i in range(n):
  array[i] = list(input())

for z in range(n-8+1):
  for k in range(m-8+1):
    cnt = 0
    for i in range(8):
      for j in range(8):        
        if version_A[i][j] != array[i+z][j+k]:
          cnt += 1
    if cnt <= min:
      min = cnt

for z in range(n-8+1):
  for k in range(m-8+1):
    cnt = 0
    for i in range(8):
      for j in range(8):        
        if version_B[i][j] != array[i+z][j+k]:
          cnt += 1
    if cnt <= min:
      min = cnt

print(min)
