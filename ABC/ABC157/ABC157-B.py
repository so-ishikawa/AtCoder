A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())

N = int(input())
b_set = set()
for i in range(N):
    b_set.add(int(input()))

sets = [set({A11,A12,A13}), set({A21,A22,A23}), set({A31,A32,A33}),
        set({A11,A21,A31}), set({A12,A22,A32}), set({A13,A23,A33}),
        set({A11,A22,A33}), set({A13,A22,A31})]

for i in sets:
    if i <= b_set:
        print("Yes")
        exit()

print("No")
