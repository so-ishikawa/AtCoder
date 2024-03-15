import math
N = int(input())
A_list = list(map(int, input().split()))

temp = [x for x in A_list if x != 0]
print(math.ceil(sum(temp)/len(temp)))
