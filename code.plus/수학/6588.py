import sys
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline().rstrip())

while n != 0:
  for i in range(3, n//2 + 1):
    if is_prime_number(i) and is_prime_number(n-i):
      print("%d = %d + %d" % (n, i, (n-i)))
      break
    if i == n//2:
      print("Goldbach's conjectrue is wrong.")
  
  n = int(sys.stdin.readline().rstrip())


