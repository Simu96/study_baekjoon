from itertools import permutations

def result(a, x):
  global min, max
  c = a[0]
  for i in range(len(a)-1):
    if x[i] == '+':
      c = add(c, a[i+1])
    elif x[i] == '-':
      c = sub(c, a[i+1])
    elif x[i] == '*':
      c = mul(c, a[i+1])
    elif x[i] == '/':
      c = div(c, a[i+1])
  
  if c >= max:
    max = c
  
  if c <= min:
    min = c

  return

def add(a, b):
  return(int(a) + int(b))

def sub(a, b):
  return(int(a) - int(b))

def mul(a, b):
  return(int(a) * int(b))

def div(a, b):  # C++14기준(음수를 양수를 나눌 때, 다른 기준 적용)
  if int(a) < 0:
    return(-(abs(int(a)) // int(b)))
  else:
    return(int(a) // int(b))


n = int(input())
a = input().split()
f = input().split()
f1 = []

max = -1000000000
min = 1000000000

for i in range(int(f[0])):
  f1.append('+')

for i in range(int(f[1])):
  f1.append('-')
  
for i in range(int(f[2])):
  f1.append('*')
  
for i in range(int(f[3])):
  f1.append('/')

# 가능한 사칙 연산 순서를 순열 리스트로 저장
f1 = list(permutations(f1, n-1))
# 집합 연산을 통해 중복되는 리스트 원소를 제거
f1_set = set(f1)
f1 = list(f1_set)

for i in range(len(f1)):
  result(a, list(f1[i]))

print(max)
print(min)
