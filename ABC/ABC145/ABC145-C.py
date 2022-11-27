import itertools
import math

N = int(input())
position_list = []
for i in range(N):
    x, y = map(int, input().split())
    position_list.append((x, y))

seq = [x for x in range(N)]
count = 0
total = 0
for i in itertools.permutations(seq):
    count += 1
    temp = 0
    for j in range(len(i)-1):
        temp += math.sqrt((position_list[i[j+1]][0] - position_list[i[j]][0])**2 + (position_list[i[j+1]][1] - position_list[i[j]][1])**2)
    total += temp
print(total/count)

