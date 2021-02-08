import sys

def fibonacci_program(n):
  a = 1 # 0 등장 횟수
  b = 0 # 1 등장 횟수
  c = 0 # 임시 저장 변수

  for i in range(n):
    c = a # 원래 a값을 임시 저장
    a = b # a값에 이전 b값 저장
    b += c # 새로운 b값 = 이전의 b값 + a값
    
  print(a, b)



t = int(sys.stdin.readline().rstrip())

for i in range(t):
  n = int(sys.stdin.readline().rstrip())
  fibonacci_program(n)
