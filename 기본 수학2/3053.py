import math

r = int(input())
u = r**2*math.pi
# 택시 기하학에서 원은 마름모 모양이 된다.(삼각형 4개)
t = r**2 / 2 * 4
print("%.6f" %u)
print("%.6f" %t)
