# 스도쿠에서 0인 부분을 좌표 배열로 저장해서 하나씩 처리하는 방법
# 각 0에 들어올 수 있는 숫자 중 행, 열, 3x3 구역을 모두 만족시키는 것을 넣어준다.
# PyPy3 형식으로 제출해야 시간초과가 발생하지 않는다.
import sys

# 행(가로) 확인
def solve_a(a, num):
  if num in s[a]:
    return False
  return True

# 열(세로) 확인  
def solve_b(b, num):
  for i in range(9):
    if num == s[i][b]:
      return False
  return True

# 3x3 구역 확인  
def solve_c(a, b, num):
  for i in range(3):
    for j in range(3):
      # (a, b)가 속해 있는 3x3 구역
      if num == s[a//3 * 3 + i][b//3 * 3 + j]:
        return False
  return True

def solve(index):
  if index == len(z): # 모든 0을 다 바꾼 후 출력
    for i in range(9):
      for j in range(9):
        print(s[i][j], end=" ")
      print("")
    sys.exit(0) # PyPy3에선 sys.exit를 사용
  else:
    for i in range(1, 10):  # 1 ~ 9의 숫자 중 세가지 조건을 모두 만족하는 숫자를 0에 대입
      # 0의 좌표(z[index][0], z[index][1])
      if solve_a(z[index][0], i) and solve_b(z[index][1], i) and solve_c(z[index][0], z[index][1], i):
        s[z[index][0]][z[index][1]] = i
        solve(index+1)
        # 정답이 없는 경우(다음 인덱스에서 답이 없으면 다시 돌아오게 되는데 그렇게 되면 처음의 스도쿠와 달라지게 된다.)를 고려하여 다시 0으로 초기화 해주어야 한다.(안하면 답 틀림)
        s[z[index][0]][z[index][1]] = 0

# 스도쿠 입력
s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 스도쿠에서 0의 위치
z = [(i, j) for i in range(9) for j in range(9) if s[i][j] == 0]

solve(0)
