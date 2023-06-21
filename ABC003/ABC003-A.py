N = int(input())
temp = 0
for i in range(1, N+1):
    temp = temp + 10000*i*(1/N)
print(temp)
