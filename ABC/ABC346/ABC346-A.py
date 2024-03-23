N = int(input())
A_list = list(map(int , input().split()))
B_list = []
for i in range(0, N-1):
    B = A_list[i]*A_list[i+1]
    print(B, end=" ")
