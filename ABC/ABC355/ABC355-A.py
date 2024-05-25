A, B = map(int, input().split())
if A == B:
    print(-1)
    exit()
temp = list([1,2,3])
temp.remove(A)
temp.remove(B)
print(temp[0])
