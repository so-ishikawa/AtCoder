import re
import itertools

M = int(input())
S1 = input()
S2 = input()
S3 = input()

temp = list(set(S1) & set(S2) & set(S3))

if len(temp) == 0:
    print(-1)
    exit()

S1 = "_" + S1 * 3
S2 = "_" + S2 * 3
S3 = "_" + S3 * 3

min_value = 999999999999999999999999
for i in temp:
    for v in itertools.permutations([S1, S2, S3]):
        index = None
        for j in range(len(v[0])):
            if i == v[0][j]:
                index = j
                break

        for j in range(index+1, len(v[1])):
            if i == v[1][j]:
                index = j
                break

        for j in range(index+1, len(v[2])):
            if i == v[2][j]:
                if min_value > j:
                    min_value = j
                break

print(min_value-1)
            
            
