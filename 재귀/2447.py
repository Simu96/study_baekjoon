def star(n):
  global array
  
  if n == 3:
    array[0][:3] = array[2][:3] = [1]  * 3
    array[1][:3] = [1, 0, 1]
    # [* * *]
    # [*   *] 입력(1은 *, 0은 공백)
    # [* * *]
    return
  else:
    n = int(n/3)
    star(n)
    for i in range(3):  # 행 증가
      for j in range(3):  # 열 증가
        if i == 1 and j ==1:  # 공백란은 유지(나머지가 1인 경우)
          continue
        else:
          for k in range(n):  # index 증가(n크기만큼)
            array[n * i + k][n * j : n * (j + 1)] = array[k][:n]

n = int(input())
array = [[0] * n for _ in range(n)]

star(n)

for i in range(n):
  for j in range(n):
    if array[i][j] == 1:
      print("*", end="")
    else:
      print(" ", end="")
  print("")
