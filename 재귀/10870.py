n = int(input())
sum = [0] * (n + 2)
sum[0] = 0
sum[1] = 1

for i in range(2, n + 1):
  sum[i] = sum[i-2] + sum[i-1]

print(sum[n])
