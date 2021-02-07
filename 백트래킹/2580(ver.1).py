# 백준 온라인 져지에서는 recursion error발생
# 스도쿠에 하나의 빈칸이라도 있다면, 행, 열, 3x3 구역을 순서대로 확인하는 방식
# 필요없는 재귀의 반복이 오류의 원인

from collections import Counter

def solve(a):
  count = 0
  
  # 스도쿠에 0이 남아 있는지 카운트
  for i in range(9):
    for j in range(9):
      if a[i][j] == 0:
        count += 1

  if count == 0:  # 스도쿠 해결
    for i in range(9):
      for j in range(9):
        print(a[i][j], end=" ")
      print("")
  else: # 재귀적으로 스도쿠 풀이
    solve_a(a)
    solve_b(a)
    solve_c(a)
    solve(a)

# 가로 풀이
def solve_a(a):
  for i in range(9):
    if Counter(a[i])[0] == 1: # 0이 하나인 경우(들어갈 수를 구할 수 있다.)
      for j in range(1, 10):
        if j not in a[i]: # 1 ~ 9 중 없는 숫자
          for k in range(9):
            if a[i][k] == 0:  # 0인 자리에 없는 숫자를 넣는다.
              a[i][k] = j
  return a

# 세로 풀이
def solve_b(a):
  for i_1 in range(9):
    cnt = 0 # 열에서 0의 개수
    c = [] # 1 ~ 9 중 없는 숫자를 찾기 위한 배열
    for i_2 in range(9):
      c.append(a[i_2][i_1]) # i_1번째 열을 배열에 저장
      if a[i_2][i_1] == 0:
        cnt += 1

    if cnt == 1: # 0이 하나인 경우(들어갈 수를 구할 수 있다.)
      for j in range(1, 10):
        if j not in c:
          for i_2 in range(9):
            if a[i_2][i_1] == 0:  # 0인 자리에 없는 숫자를 넣는다.
              a[i_2][i_1] = j

  return a

# 3 x 3 풀이
def solve_c(a):
  # eg) a[2][3] => (i_1 * 3 + i_2)번째 행, (j_1 * 3 + j_2)번째 열
  for i_1 in range(3):
    for j_1 in range(3):
      cnt = 0 # 구역 안에서 0의 개수
      c = [] # 1 ~ 9 중 없는 숫자를 찾기 위한 배열
      for i_2 in range(3):
        for j_2 in range(3):
          c.append(a[3 * i_1 + i_2][3 * j_1 + j_2]) # 3 x 3으로 나눈 구역의 수를 배열에 저장
          if a[3 * i_1 + i_2][3 * j_1 + j_2] == 0:
            cnt += 1

      if cnt == 1:  # 0이 하나인 경우(들어갈 수를 구할 수 있다.)
        for h in range(1, 10):
          if h not in c:
            for i_2 in range(3):
              for j_2 in range(3):
                if a[3 * i_1 + i_2][3 * j_1 + j_2] == 0:  # 0인 자리에 없는 숫자를 넣는다.
                  a[3 * i_1 + i_2][3 * j_1 + j_2] = h

  return a

# 스도쿠 배열 초기화
s = [[0] * 9 for _ in range(9)]

# 스도쿠 입력
for i in range(9):
  s[i] = list(map(int, input().split()))

solve(s)
