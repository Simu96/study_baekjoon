# n : 개수, a : 시작, b : 거쳐가는 곳, c : 목적지
def hanoi(n, a, b, c):
  if n == 1:
    # n = 1일 떄, 1번째에서 3번째로 가면 된다.
    print(a, c)
  else:
    # 그 외의 경우 하나 작은 수를 n자리에, 기존 목적지를 경유지에 넣는다.(그 전의 경우를 두번째(경유지)에 옮겨야 하므로)
    hanoi(n-1, a, c, b)
    # 그 다음, 맨 아래 수를 목적지로 옮긴다.
    print(a, c)
    # 이후 경유지로 옮겼던 이전 케이스를 첫번째를 경유해 목적지 위에 쌓는다.
    hanoi(n-1, b, a, c)  
  return

n = int(input())

cnt = 2**n - 1
print(cnt)
hanoi(n, 1, 2, 3)
