import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
  a.append(sys.stdin.readline().rstrip())

# 알파벳 순으로 정렬
a.sort()
# 길이 순으로 다시 정렬
a.sort(key = lambda a : len(a))

for i in range(n):
  if i > 0 and a[i] == a[i-1]:
    continue
  else:
    print(a[i])
