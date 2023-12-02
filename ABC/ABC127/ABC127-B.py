r, D, x2000 = map(int, input().split())

def f(temp):
    return(r*temp-D)

x = x2000
for i in range(10):
    x = f(x)
    print(x)
