N = int(input())

set_ = set({})
for i in range(1, 9+1):
    for j in range(1, 9+1):
        set_.add(i*j)
if N in set_:
    print("Yes")
    exit()
print("No")
