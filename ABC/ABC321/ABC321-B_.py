N, X = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

# max case
temp = X - sum(A_list[1:])
if 100 >= temp and temp >= A_list[-1]:
    print(A_list[-1])
    exit()

# min case
temp = X - sum(A_list[:-1])
if A_list[0] >= temp and temp >= 0:
    print(A_list[0])
    exit()

# etc case
temp = X - sum(A_list[1:-1])
if 
