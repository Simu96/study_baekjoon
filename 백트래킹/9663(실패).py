def q_count(x):
  cnt = 0
  global total_cnt, n
  for i in range(n):
    for j in range(n):
      if x[i][j] == 0:
        x[i][j] = 2
        cnt += 1
            
        index = 1
        while(i + index < n):
          x[i+index][j] = 1
          index += 1
              
        index = 1
        while(i - index >= 0):
          x[i-index][j] = 1
          index += 1

        index = 1
        while(j + index < n):
          x[i][j+index] = 1
          index += 1

        index = 1
        while(j - index >= 0):
          x[i][j-index] = 1
          index += 1

        index = 1
        while(i + index < n and j + index < n):
          x[i+index][j+index] = 1
          index += 1

        index = 1
        while(i - index >= 0 and j - index >= 0):
          x[i-index][j-index] = 1
          index += 1
              
        index = 1
        while(i + index < n and j - index >= 0):
          x[i+index][j-index] = 1
          index += 1

        index = 1
        while(i - index >= 0 and j + index < n):
          x[i-index][j+index] = 1
          index += 1
  if cnt == n:
    total_cnt += 1
    print(x)
    print("this case")

  return
    

n = int(input())
a = [[0] * n for _ in range(n)]
c = [0] * n * n

print(c)

total_cnt = 0

q_count(a)
a = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    a[i][j] = 1
    

print(total_cnt)
