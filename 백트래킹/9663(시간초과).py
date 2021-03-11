# 정담(시간초과)
import sys

def check(x, index_r, index_c):
  global n

  if index_r == 0:  # 1번째 행일 때
    x[index_r][index_c] = True
    return True
  
  for i in range(1, index_r+1):
    if x[index_r-i][index_c] == True: # 같은 열 false
      return False
  
  for i in range(1, index_r+1): # 대각선 false(왼쪽 위, 오른쪽 위)
    if index_c-i >= 0 and x[index_r-i][index_c-i] == True:
      return False
  
    if index_c+i < n and x[index_r-i][index_c+i] == True:
      return False

  x[index_r][index_c] = True
  return True
  


def after_check(x, index_r, index_c):
  x[index_r][index_c] = 0


def dfs(row_n):
  global n, a, total_cnt

  if row_n == n:  # 마지막 행에서까지 true여야한다. n-1 아님
    total_cnt += 1
    #for i in range(n):  # 조건을 만족하는 경우를 출력할 수 있다.
    #  print(a[i])
    #print("-------------")
  else:
    for i in range(n):
      if check(a, row_n, i):
        dfs(row_n+1)
        after_check(a, row_n, i)  # 가능한 깊이까지 탐색 후 초기화해준다.
  


n = int(sys.stdin.readline().rstrip())
a = [[0] * n for _ in range(n)]
total_cnt = 0
dfs(0)
print(total_cnt)

