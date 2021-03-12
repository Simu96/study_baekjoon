def brute_fore(n):
  for i in range(1, 1000001):
    sum = 0
    sum += i
    char = str(i)
    for j in range(len(char)):
     sum += int(char[j])
 
    if sum == n:
      print(i)
      break
  if i == 1000000:
    print("0")
  
n = int(input())
brute_fore(n)
