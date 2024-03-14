N = int(input())
a, b = map(int, input().split())
K = int(input())
P_list = list(map(int, input().split()))

set_ = set(P_list)
set_.add(a)
set_.add(b)

if len(set_) == K+2:
    print("YES")
    exit()
print("NO")

