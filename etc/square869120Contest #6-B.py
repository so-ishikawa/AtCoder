import math
n = int(input()) 
AB_list = []

min_point = 1000000000
max_point = 1

for i in range(n):
    A, B = map(int, input().split())
    AB_list.append((A, B))

    if min_point > A:
        min_point = A
    if max_point < B:
        max_point = B

AB_length_list = []
for i in AB_list:
    AB_length_list.append(math.sqrt((i[0] - i[1])**2))

result_min_length = 0

for start in range(min_point, max_point+1):
    for end in range(start, max_point+1):
        reverse_point_list = [False] * len(AB_list)
        for i in AB_list:
            
