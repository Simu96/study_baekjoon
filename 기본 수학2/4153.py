x, y, z = 0, 0, 0
while(1):
  x, y, z = map(int, input().split())
  if x == 0 and y == 0 and z == 0:
    break
  if z**2 == x**2 + y**2 or x**2 == y**2 + z**2 or y**2 == z**2 + x**2:
    print("right")
  else:
    print("wrong")
