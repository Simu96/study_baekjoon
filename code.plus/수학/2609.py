import sys
import math

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

gcd = math.gcd(n1, n2)
print(gcd)
print(gcd * (n1 // gcd) * (n2 // gcd))
