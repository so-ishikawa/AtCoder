N, X = map(int, input().split())
A_list = list(map(int, input().split()))

for i in A_list:
    if i == X:
        continue
    print(i, end=" ")
