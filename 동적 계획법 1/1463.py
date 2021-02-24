import sys

n = int(sys.stdin.readline().rstrip())
count = [i for i in range(n+1)] # 0부터 n까지 숫자의 최저 연산 횟수를 저장하는 배열

count[0] = 0
if n > 0: # 런타임 에러 방지(index error)
  count[1] = 0  # 1의 경우 추가 연산 필요 없음

for i in range(2, n+1):
  # 기본적으로 i를 만들 때 필요한 연산 횟수는 i-1을 만드는데 필요한 연산 횟수 +1이다.
  count[i] = count[i-1] + 1

  # i가 3으로 나누어 떨어지는 경우, 3으로 나누었을 때 나온 숫자를 만드는데 필요한 연산 횟수와 기본적으로 i-1을 만드는데 필요한 연산 횟수를 비교해 적은 연산 횟수를 선택한다. 
  if i % 3 == 0:
    count[i] = min(count[i//3], count[i-1]) + 1
  
  # i가 2로 나누어 떨어지는 경우
  if i % 2 == 0:
    count[i] = min(count[i//2], count[i-1]) + 1
  
  # i가 2와 3으로 나누어 떨어지는 경우
  if i % 3 == 0 and i % 2 == 0:
    count[i] = min(count[i//3], count[i//2], count[i-1]) + 1

print(count[n])
