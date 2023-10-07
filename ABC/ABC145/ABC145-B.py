N = int(input())
S = input()

if len(S) % 2 == 1:
    print("No")
    exit()

if S[:len(S)//2] == S[-1*(len(S)//2):]:
    print("Yes")
    exit()

print("No")
exit()
