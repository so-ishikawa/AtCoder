N = int(input())
A = list(map(int, input().split()))

diff = A[1]/A[0]

for i in range(len(A)-1):
    if A[i+1]*A[0] == A[1]* A[i]:
        continue
    print("No")
    exit()
print("Yes")
