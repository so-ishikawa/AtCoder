N, S = map(int, input().split())
A_list = list(map(int, input().split()))

sum_ = sum(A_list)
target = S % sum_

A_list.append("_") #dummy
set_ = set()

for i in range(len(A_list)-1):
    for j in range(i+1, len(A_list)):
        set_.add(sum(A_list[i:j]))

if target in set_:
    print("Yes")
    exit()
print("No")
