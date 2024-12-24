N, A, B = map(int, input().split())
D_list = list(map(int, input().split()))

D_list.sort()

for i in range(len(D_list)):
    if i == len(D_list)-1:
        if (D_list[i] - D_list[0]) % (A + B) <= A:
            print("Yes")
            exit()
    if not ((D_list[i+1] - D_list[i]) % (A + B) <= A):
        print("No")
        exit()
        
