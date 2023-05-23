N, M, D = map(int, input().split())
A_list = sorted(list(map(int, input().split())))
B_list = sorted(list(map(int, input().split())))

# A_list.sort()
# B_list.sort()

a = A_list.pop()
b = B_list.pop()

while True:

    if abs(a - b) <= D:
        print(a+b)
        exit()

    if A_list and B_list:
        if a < b:
            b = B_list.pop()
            continue
    
        if a > b:
            a = A_list.pop()
            continue
    else:
        break
print(-1)
