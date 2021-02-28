# 시간초과로 PyPy3로 제출
import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))

s_1 = [0 for _ in range(n)] # 자신을 포함하는 최대 증가 수열 길이를 저장하는 배열
s_1[0] = 1  # 한자리 수열의 값은 1


for i in range(1, n):
  max_s = 0
  # 이전까지의 숫자들 중 자신보다 작은 숫자를 찾아 그 중 최대 길이에 1을 더해준다.
  for j in range(i):
    if a[j] < a[i]:
      if max_s < s_1[j]:
        max_s = s_1[j]
    
    s_1[i] = max_s + 1  # 자신보다 작은 숫자가 없다면 0 + 1, 최대 길이 1이 된다.

s_3 = [0 for _ in range(n)] # i번째 이후 감소하는 수열 중 가장 길이가 짧은 수열의 길이를 저장하는 배열

for i in range(n-1):
  s_2 = [0 for _ in range(n)] # 자신을 포함하는 최대 감소 수열 길이를 저장하는 배열

  # i 이후의 숫자들에서 작아지는 수열의 길이를 저장하는 부분(i부분보다 작으면 자신(j)과 i번 사이에 있는 것들 중 자신보다 큰 숫자들 중 가장 긴 수열 길이에 1을 더해준다.)
  for j in range(i+1, n):
    if a[i] > a[j]: # i번째 숫자보다 작은 경우, i번째를 기준으로 작아지는 수열을 만들 수 있다.
      max_s = 0
      for k in range(i+1, j):
        if a[k] > a[j]:
          if max_s < s_2[k]:
            max_s = s_2[k]
        
      s_2[j] = max_s + 1  # 자신보다 큰(i보다는 작고) 숫자가 없다면 0 + 1, 최대 길이 1이 된다.
    else: # i번째 숫자보다 큰 경우, i번째를 기준으로 작아지는 수열이 만들어지 않는다.(길이 : 0)
      s_2[j] = 0

  # i 이후, 작아지는 수열에서 길이가 가장 긴 경우를 s_3배열에 저장해준다.
  s_3[i+1] = max(s_2)

# i번째까지 최대 길이 증가 수열 + i번째 이후 최대 길이 감소 수열 중 최댓값을 찾아 total_max에 저장한다.
total_max = 1 # 한자리 수열의 최댓값은 1
for i in range(n-1):
  if s_1[i] + s_3[i+1] > total_max:
    total_max = s_1[i] + s_3[i+1]

print(total_max)
