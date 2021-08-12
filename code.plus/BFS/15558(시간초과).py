import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
left_list = list(map(int, sys.stdin.readline().rstrip()))
right_list = list(map(int, sys.stdin.readline().rstrip()))

sec = 0
result = 0

queue = deque()
direction = "left"
queue.append((0, direction, sec))

while queue:
  l, dir, sec = queue.popleft()

  if dir == "left":
    if l+1 < n and left_list[l+1] != 0:
      # 같은 줄에서 한칸 전진
      queue.append((l+1, "left", sec+1))
    if left_list[l-1] != 0 and l > 1:
      if l-1 > sec:
        # 같은 줄에서 한칸 후진
        queue.append((l-1, "left", sec+1))
    if l+k < n and right_list[l+k] != 0:
      # 다른 줄에서 k칸 전진
      queue.append((l+k, "right", sec+1))

  if dir == "right":
    if l+1 < n and right_list[l+1] != 0:
      queue.append((l+1, "right", sec+1))
    if right_list[l-1] != 0 and l > 1:
      if l-1 > sec:
        queue.append((l-1, "right", sec+1))
    if l+k < n and left_list[l+k] != 0:
      queue.append((l+k, "left", sec+1))

  # 탈출 판단
  if l+1 >= n:
    result = 1
    break

  if l+k >= n:
    result = 1
    break

print(result)
