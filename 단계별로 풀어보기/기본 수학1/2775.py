t = int(input())
for i in range(t):
  k = int(input())
  n = int(input())
  
  # k = 0층부터 시작이므로 range에서 + 1
  array = [[0] * n for _ in range(k + 1)]
  for i in range(n):
    array[0][i] = i+1

  for i in range(k + 1):
    array[i][0] = 1
  
  for i in range(1, k + 1):
    for j in range(1, n):
      array[i][j] = array[i - 1][j] + array[i][j - 1]

  # 행렬 확인
  # for i in range(k + 1):
  #   print(array[i])
  
  print(array[k][n-1])

      


