n = int(input())
weight = [0] * n
height = [0] * n
cnt = [1] * n

for i in range(n):
  weight[i], height[i] = map(int, input().split())

for i in range(n):
  for j in range(n):
    if i == j:
      continue
    else:
      if weight[j] > weight[i] and height[j] > height[i]:
        cnt[i] += 1

for i in range(n):
  print(cnt[i], end=" ")
