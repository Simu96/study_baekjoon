x = [0] * 3
y = [0] * 3

for i in range(3):
  x[i], y[i] = map(int, input().split())

result_x = [True] * 1001
result_y = [True] * 1001

for i in range(3):
  if result_x[x[i]] == True:
    result_x[x[i]] = False
  else:
    result_x[x[i]] = True
  
  if result_y[y[i]] == True:
    result_y[y[i]] = False
  else:
    result_y[y[i]] = True

for i in range(1001):
  if result_x[i] == False:
    print(i, end=" ")

for i in range(1001):
  if result_y[i] == False:
    print(i)
