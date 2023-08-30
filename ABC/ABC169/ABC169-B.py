N = int(input())
A_list = list(map(int, input().split()))
A_set = set(A_list)

if 0 in A_set:
    print(0)
    exit()

A_list.sort(reverse=True)

temp = 1
for i in A_list:
    temp = temp * i
    if temp > 10**18:
        print(-1)
        exit()
        
print(temp)

