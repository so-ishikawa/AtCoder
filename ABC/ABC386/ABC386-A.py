A, B, C, D = map(str, input().split())

set_ = set({A, B, C, D})
if len(set_) != 2:
    print("No")
    exit()

print("Yes")
