import sys
n = int(sys.stdin.readline().rstrip())

a = [0] * n

for i in range(n):
  a[i] = int(sys.stdin.readline().rstrip())

a = sorted(a)

# print(sorted(a)[i]) 이런식으로 하면 sort가 반복문마다 이뤄지므로 시간초과
for i in range(n):
  print(a[i])
