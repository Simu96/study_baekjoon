n = int(input())
array = [0] * n
for i in range(n):
  array[i] = int(input())


for i in range(n):
  print(sorted(array)[i])
