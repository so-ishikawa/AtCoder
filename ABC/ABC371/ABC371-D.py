import bisect
N = int(input())
X_list = list(map(int, input().split()))
P_list = list(map(int, input().split()))

exist_X_set = set(X_list)

sum_ = []
for i in P_list:
    if len(sum_) == 0:
        sum_.append(i)
        continue
    sum_.append(sum_[-1]+i)
sum_.insert(0, 0)

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    
    l = bisect.bisect_left(X_list, L)
    r = bisect.bisect_right(X_list, R)
    print(sum_[r]-sum_[l])
