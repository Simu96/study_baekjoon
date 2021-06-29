import sys
from itertools import combinations

s = list(map(int, sys.stdin.readline().rstrip().split()))

while s[0] != 0:
  del s[0]
  x = list(combinations(s, 6))
  
  for i in range(len(x)):
    for j in range(len(x[i])):
      print(x[i][j], end = " ")
    print("")
  print("")

  s = list(map(int, sys.stdin.readline().rstrip().split()))
