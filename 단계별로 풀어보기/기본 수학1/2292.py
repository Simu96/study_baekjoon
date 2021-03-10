n = int(input())

# r = i번째 줄까지의 방 개수(eg.3번째 줄까지의 방 개수 r = 1 + 6 + 12 = 19개)
r = 1
i = 1

while(n > r):
  r += 6 * i  
  i += 1

print(i)    
