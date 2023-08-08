N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

temp = ""
for i in range(N):
    if i == 0:
        temp = set(range(A_list[i], B_list[i]+1))
        continue
    temp = temp & set(range(A_list[i], B_list[i]+1))
    
print(len(temp))
