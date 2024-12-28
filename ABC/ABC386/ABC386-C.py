K = int(input())
S = input()
T = input()

if S == T:
    print("Yes")
    exit()

if len(S) == len(T):
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count+=1
    if count == 1 or count == 0:
        print("Yes")
    else:
        print("No")
    exit()

if len(S) > len(T):
    if len(S) - len(T) != 1:
        print("No")
        exit()

    diff = 0
    for i in range(len(T)):
        i_ = i + diff
        if S[i] != T[i_]:
            if diff == 1:
                print("No")
                exit()
            diff = 1
        if i == len(S)-1 and diff == 1:
            print("No")
            exit()
    print("Yes")

        

if len(S) < len(T):
    if len(T) - len(S) != 1:
        print("No")
        exit()

    diff = 0
    for i in range(len(S)):        
        i_ = i + diff

        if S[i] != T[i_]:
            if diff == 1:
                print("No")
                exit()
            if i == len(S)-1:
                print("No")
                exit()
            diff = 1
    print("Yes")
