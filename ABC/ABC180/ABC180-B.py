import math

N = int(input())
X_list = list(map(int, input().split()))

man = sum([math.fabs(x) for x in X_list])
yu = sum([(math.fabs(x))**2 for x in X_list])**(1/2)
tye = max([math.fabs(x) for x in X_list])

print(man)
print(yu)
print(tye)
