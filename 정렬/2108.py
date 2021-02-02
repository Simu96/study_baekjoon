import sys
from collections import Counter

n = int(sys.stdin.readline())
a = [0] * n

for i in range(n):
  a[i] = int(sys.stdin.readline())

# 산술 평균
print(round(sum(a) / len(a)))

# 중간값
a.sort()
cen = int(n / 2)
print(a[cen])

# 최빈값
cnt_a = Counter(a)
b = cnt_a.most_common()

# 이 부분 빼먹어서 계속 IndexError(숫자가 하나일 경우에는 비교문에서 indexError가 난다.)
if len(a) > 1:
  if b[0][1] == b[1][1]:
    print(b[1][0])
  else:
    print(b[0][0])
else:
  print(b[0][0])

# 범위
print(max(a) - min(a))
