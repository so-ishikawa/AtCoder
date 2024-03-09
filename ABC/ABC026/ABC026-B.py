import math

N = int(input())
R_list = []
for _ in range(N):
    R_list.append(int(input()))

R_list.sort(reverse=True)

if N % 2 != 0:
    R_list.append(0)

temp = 0
for i in range(0, len(R_list), 2):
    temp += R_list[i]**2 - R_list[i+1]**2

print(temp*math.pi)
