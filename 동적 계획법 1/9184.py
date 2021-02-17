# 재귀함수에서 이미 계산했던 값을 저장해두고 다시 사용하는 방법 : 메모이제이션(시간을 단축할 수 있다.)
# 시간 제한으로 PyPy3 형태로 제출
import sys

def w(a, b, c):
  global memoization

  if (a, b, c) in memoization.keys():  # 이미 계산된 값
    return memoization[(a, b, c)] # (a, b, c)경우의 value값 return

  if a <= 0 or b <= 0 or c <= 0:
    return 1
  elif a > 20 or b > 20 or c > 20:
    memoization[(20, 20, 20)] = w(20, 20, 20)
    return memoization[(20, 20, 20)]
  elif a < b and b < c:
    memoization[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return memoization[(a, b, c)]
  else:
    memoization[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memoization[(a, b, c)]


while(1):
  a, b, c = map(int, sys.stdin.readline().split())
  if a == -1 and b == -1 and c == -1:
    break

  memoization = dict()
  print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
