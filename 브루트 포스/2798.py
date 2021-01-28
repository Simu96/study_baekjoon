n, m = map(int, input().split())
max = 0
array = list(map(int, input().split()))

for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if array[i] + array[j] + array[k] <= m:
        if array[i] + array[j] + array[k] >= max:
          max = array[i] + array[j] + array[k]

print(max)
