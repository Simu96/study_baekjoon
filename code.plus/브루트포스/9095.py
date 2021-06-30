import sys
import math

t = int(sys.stdin.readline().rstrip())

for i in range(t):
  m = int(sys.stdin.readline().rstrip())
  count = 0
  c = 0
  p = 0
  for j in range((m // 3) + 1):
    for k in range((m // 2) + 1):
      for z in range(m + 1):
        c = j * 3 + k * 2 + z * 1 

        if c == m:
          # 중복된 원소를 사용한 순열의 개수를 구하는 공식
          count += int(math.factorial(j + k + z) / math.factorial(j) / math.factorial(k) / math.factorial(z))
          c = 0
        else:
          c = 0

  print(count)
