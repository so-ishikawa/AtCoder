N = int(input())
S = input()
N = S
if len(S) % 2 == 0:
    print("No")
    exit()

if N[len(N)//2] != "/":
    print("No")
    exit()

if N[0:len(N)//2] == "1"*(len(N)//2) and N[len(N)//2+1:len(N)] == "2"*(len(N)//2):
    print("Yes")
    exit()
print("No")
