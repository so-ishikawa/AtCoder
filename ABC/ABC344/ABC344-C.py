N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))
L = int(input())
C_list = list(map(int, input().split()))
Q = int(input())
X_list = list(map(int, input().split()))

set_ = set()
for a in A_list:
    for b in B_list:
        for c in C_list:
            set_.add(a+b+c)

for x in X_list:
    if x in set_:
        print("Yes")
    else:
        print("No")
