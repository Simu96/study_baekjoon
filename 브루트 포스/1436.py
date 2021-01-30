# 6661, 6662 같은 case 주의하기!
n = int(input())

a = '666'
cnt = 0

while(1):
  if '666' in a:
    cnt += 1

  if cnt == n:
    break
  a = int(a) + 1
  a = str(a)

print(a)
