x = int(input())

n = 1   # i번째 줄까지의 원소 개수
i = 1   # x가 속하는 줄
k = 0   # i-1번째 줄까지의 원소 개수(n에서 k를 빼주면 x가 해당하는 줄의 원소 수를 알 수 있다.)

while(x > n):
  i += 1
  n += i

for j in range(i):
  k += j

if i % 2 == 0:  # x가 짝수 줄에 속하는 경우
  print(x - k, end = "")
  print("/", end = "") 
  print(i - x + k + 1)
else:   # x가 홀수 줄에 속하는 경우
  print(i - x + k + 1, end = "")
  print("/", end = "") 
  print(x - k)
