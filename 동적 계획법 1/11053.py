import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))

s = [0 for _ in range(n)] # 자신을 포함하는 최대 수열 길이를 저장하는 배열
s[0] = 1  # 한자리 수열의 값은 1

for i in range(1, n):
  max_s = 0
  # 이전까지의 숫자들 중 자신보다 작은 숫자를 찾아 그 중 최대 길이에 1을 더해준다.
  for j in range(i):
    if a[j] < a[i]:
      if max_s < s[j]:
        max_s = s[j]
    
    s[i] = max_s + 1  # 자신보다 작은 숫자가 없다면 0 + 1, 최대 길이 1이 된다.
      

print(max(s)) # 가장 긴 길이 출력
