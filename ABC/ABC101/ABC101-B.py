N = int(input())

def f(n):
    temp = 0
    for i in range(len(str(n))):
        temp += int((str(n))[i])
    return(temp)
# print(f(12))
if N % f(N) == 0:
    print("Yes")
    exit()
print("No")
