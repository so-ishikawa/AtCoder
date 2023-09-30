N = int(input())
S = input()

if S.find("ABC") == -1:
    print(-1)
    exit()
print(S.find("ABC")+1)
