from itertools import combinations
import math

# combination을 사용 : team_a가 a[i]구성이라면 team_b의 선수 구성은 a[n-i]가 된다.
# eg) n = 4일 때, combination 사용 => 나오는 팀 경우 : (0, 1), (0, 2), (0, 3) / (1, 2), (1, 3), (2, 3) => (0, 1)과 (2, 3)이 한 경우!!
def team_making(a):
  global s
  # 양의 무한대로 우선 설정
  min = math.inf

  # 팀의 능력치 합 경우를 저장할 변수
  team_a_sum = []
  team_b_sum = []

  # team_A
  for i in range(len(a)//2):  # 처음부터 중간까지 선수 조합을 기준으로
    # 팀원 시너지 조합
    b = list(combinations(a[i], 2))
    sum = 0
    for j in range(len(b)):
      sum += s[b[j][0]][b[j][1]] + s[b[j][1]][b[j][0]]

    team_a_sum.append(sum)

  # team_B(역순으로 저장)
  for i in range(len(a)-1, len(a)//2-1, -1): # 중간부터 끝까지 선수 조합을 기준으로
    # 팀원 시너지 조합(2명씩 시너지)
    c = list(combinations(a[i], 2))
    sum = 0
    for j in range(len(c)):
      sum += s[c[j][0]][c[j][1]] + s[c[j][1]][c[j][0]]
    
    team_b_sum.append(sum)

  # 각 팀의 시너지를 비교해 최솟값을 저장
  for k in range(len(team_a_sum)):
    if abs(team_a_sum[k] - team_b_sum[k]) <= min:
      min = abs(team_a_sum[k] - team_b_sum[k])

  # 최솟값 출력
  print(min)


n = int(input())
n_1 = [0] * n
s = [0] * n

for i in range(n):
  n_1[i] = i  # 선수 번호(0번부터)
  s[i] = list(map(int, input().split()))  # 능력치

# 팀 조합(n명을 2개의 팀으로))
a = list(combinations(n_1, n//2))
team_making(a)

