t = int(input())
c = 0

for i in range(t):
  x, y = map(int, input().split())
  distance = y - x
  j = 0
  j_sum = 0
  j_c = 0
  k = 0
  k_sum = 0
  k_c = 0

  while(j_sum + k_sum < distance):
    j += 1
    j_c += 1
    j_sum += j
    c = j_c + k_c
    if j_sum + k_sum >= distance:
      break

    k += 1
    k_c += 1
    k_sum += j
    c = j_c + k_c
  
  print(c)

  
