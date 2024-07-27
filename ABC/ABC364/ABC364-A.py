N = int(input())
flag = False
for i in range(N):
    s = input()
    if s == "sweet":
        if flag and i != N-1:
            print("No")
            exit()
        flag = True
        continue
    flag = False
print("Yes")
