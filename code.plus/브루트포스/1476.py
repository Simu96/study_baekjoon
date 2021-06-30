import sys

e, s, m = map(int, sys.stdin.readline().rstrip().split())
i, j, k = 1, 1, 1
count = 1;

while i != e or j != s or k != m:
  count += 1
  i += 1
  j += 1
  k += 1
  if i > 15:
    i = 1
  if j > 28:
    j = 1
  if k > 19:
    k = 1
  
print(count)
