import math

t = int(input())
for i in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

  if r1 == r2 and distance == 0:
    print("-1")
  elif distance > (r1 + r2):
    print("0")
  elif distance == (r1 + r2): # 외접
    print("1")
  elif (distance + r1) == r2 or (distance + r2) == r1: # 내접
    print("1")
  elif r2 > (distance + r1) or r1 > (distance + r2):
    print("0")
  else:
    print("2")
