# 인덱스를 증가시켜가며 모든 경우의 수를 찾으려했지만, 인덱스를 증가시키며 찾으면 찾을 수 없는 경우가 존재. 새로운 방법으로 풀어야함.
# 찾을 수 없는 경우
# 1 1 1 2 1
# 0 0 1 1 1
# 0 1 0 1 0   =>  이 경우, 무조건 (1, 1)에 2를 대입하게 되어서 
# 1 0 0 1 0       (1, 2)이 2인 경우를 찾지 못한다.
# 0 0 0 1 0
import sys

def q_count(x, index_x, index_y):
  global n, total_cnt
  cnt = 0
  
  for i in range(index_x+1):
    if i == index_x:
      for j in range(index_y+1):
        x[i][j] = 1
    else:
      for j in range(n):
        x[i][j] = 1

  print("before")
  for i in range(n):
    print(x[i])

  for i in range(n):
    for j in range(n):
      if x[i][j] == 0:
        cnt += 1

        for k in range(n):  # 같은 행, 열에 놓지 못한다.
          x[i][k] = 1
          x[k][j] = 1
        
        for k in range(min(n-i, n-j)):  # 대각선(오른쪽 아래 방향)에 놓지 못한다.
          x[i+k][j+k] = 1

        for k in range(min(i, j)+1):  # 대각선(왼쪽 위 방향)에 놓지 못한다.
          x[i-k][j-k] = 1

        for k in range(min(i, n-j-1)+1):  # 대각선(오른쪽 위 방향)에 놓지 못한다.
          x[i-k][j+k] = 1

        for k in range(min(n-i-1, j)+1):  # 대각선(오른쪽 아래 방향)에 놓지 못한다.
          x[i+k][j-k] = 1

        x[i][j] = 2 # 제자리에는 퀸을 놓을 수 있다.
  print("after")
  for i in range(n):
    print(x[i])

  if cnt >= n:  # 최종 결과 체스판에 n개 이상의 퀸이 있다면 경우의 수로 카운트
    print("this")
    total_cnt += 1
  return x
    

n = int(sys.stdin.readline().rstrip())
a = [[0] * n for _ in range(n)]
total_cnt = 0

q_count(a, -1, -1)

for i in range(n):
  for j in range(n):
    a = [[0] * n for _ in range(n)]
    q_count(a, i, j)

print(total_cnt)
