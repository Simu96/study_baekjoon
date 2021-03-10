n = int(input())

n1 = n
c = 0

while(1):
  if n1 > 0 and n1 % 5 == 0:
    c += int(n1/5)
    break
  elif n1 == 0:
    c = int(n/3)
    break
  elif n1 < 0:
    c = -1
    break
  
  n1 -= 3
  c += 1

print(c)


