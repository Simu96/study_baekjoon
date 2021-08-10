import sys
from collections import deque

a, b, c = map(int,(sys.stdin.readline().rstrip().split()))

result = []
check = [[0] * (201) for _ in range(201)]

def bfs():
  queue = deque()
  queue.append((0, 0))
  check[0][0] = 1

  while queue:
    x, y = queue.popleft()
    z = c - (x + y)
    if x == 0:
      result.append(z)

    if x>0 and y<b: # a에서 b로 물을 붓는 경우
      water = min(x, b-y) # 옮겨지는 물의 양
      if check[x-water][y+water] == 0:
        check[x-water][y+water] = 1
        queue.append((x-water, y+water))
    
    if x>0 and z<c: # a에서 c
      water = min(x, c-z)
      if check[x-water][y] == 0:
        check[x-water][y] = 1
        queue.append((x-water, y))

    if y>0 and x<a: # b에서 a
      water = min(y, a-x)
      if check[x+water][y-water] == 0:
        check[x+water][y-water] = 1
        queue.append((x+water, y-water))
    
    if y>0 and z<c: # b에서 c
      water = min(y, c-z)
      if check[x][y-water] == 0:
        check[x][y-water] = 1
        queue.append((x, y-water))

    if z>0 and x<a: # c에서 a
      water = min(z, a-x)
      if check[x+water][y] == 0:
        check[x+water][y] = 1
        queue.append((x+water, y))

    if z>0 and y<b: # c에서 b
      water = min(z, b-y)
      if check[x][y+water] == 0:
        check[x][y+water] = 1
        queue.append((x, y+water))

bfs()

result = sorted(result)
for i in range(len(result)):
  print(result[i], end=' ')
