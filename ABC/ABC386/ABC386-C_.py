K = int(input())
S = list(input())
T = list(input())

if len(S) == len(T):
    flag = False
    for i in range(len(S)):
        if S[i] != T[i]:
            if flag:
                print("No")
                exit()
            flag = True
    print("Yes")
    exit()

if len(S) - len(T) == 1:
    flag = False
    for i in range(len(T)):
        if S[i] != T[i]:
            if flag:
                print("No")
                exit()
            S.pop(i)
            if S[i] != T[i]:
                print("No")
                exit()
            flag = True
    print("Yes")
    exit()

if len(S) - len(T) == -1:
    flag = False
    for i in range(len(S)):
        if S[i] != T[i]:
            if flag:
                print("No")
                exit()
            S.insert(i, "_")
            flag = True
    print("Yes")
    exit()

print("No")
