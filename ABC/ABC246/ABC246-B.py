A, B = map(int, input().split())

if A == 0:
    if B > 0:
        print(0, 1)
        exit()
    print(0, -1)
    exit()


a = (1/(1+(B*B/(A*A))))**(1/2)
b = a*(B/A)
print(a,b)
