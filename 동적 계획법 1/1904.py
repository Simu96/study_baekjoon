import sys

n = int(sys.stdin.readline().rstrip())
a = [0] * 1000001 # [0] * n으로 하면 n = 1인 경우 index error
a[0] = 1  # n이 1인 경우
a[1] = 2  # n이 2인 경우
for i in range(2, n):
  # n = 3일 때 부터, n - 1 번째에 1을 붙이는 경우 + n - 2번째에 00을 붙이는 경우를 더해주면 n의 경우의 수가 나온다
  a[i] = (a[i-1] + a[i-2]) % 15746  #  결과값에만 해주면 메모리 초과 발생
  
print(a[n-1])
