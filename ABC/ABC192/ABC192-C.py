def g1(num):
    temp = list(str(num))
    temp.sort(reverse=True)
    return(int("".join(temp)))

def g2(num):
    temp = list(str(num))
    temp.sort()
    return(int("".join(temp)))

def f(num):
    return(g1(num)-g2(num))

N, K = map(int, input().split())
temp = N

for i in range(K):
    temp = f(temp)
    
print(temp)
