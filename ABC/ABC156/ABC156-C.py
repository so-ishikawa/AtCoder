import math
N = int(input())
X_list = list(map(int, input().split()))

temp = sum(X_list)/len(X_list)
a = math.ceil(temp)
b = int(temp)

a = sum([(x-a)**2 for x in X_list])
b = sum([(x -b)**2 for x in X_list])

print(min(a,b))
