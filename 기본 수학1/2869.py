a, b, v = map(int, input().split())

if a == v:  # 하루만에 갈 수 있는 높이
  n = 1
else: # 낮 동안 갈 수 있는 거리를 제외하고 날짜 수를 계산
  if (v - a) % (a - b) == 0: 
    n = 1 + int((v - a) / (a - b))
  else:
    n = 1 + int((v - a) / (a - b) + 1)

print(n)
