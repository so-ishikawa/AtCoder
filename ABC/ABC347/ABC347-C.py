N, A, B = map(int, input().split())
D_list = list(map(int, input().split()))

temp = [d % (A+B) for d in D_list]
temp.sort()

temp = temp + [d + (A+B) for d in temp]
# bprint(temp)
for i in range(len(temp)-1):
    """
    if i == len(temp)-1:
        if abs(temp[i]-temp[0]) >= B:
            print("Yes")
            exit()
        print("No")
        exit()
    """
    if temp[i+1] - temp[i] >= B+1:
        print("Yes")
        exit()
print("No")
