A = int(input())
B = int(input())
C = int(input())

temp = [A, B, C]
temp.sort(reverse=True)

print(temp.index(A)+1)
print(temp.index(B)+1)
print(temp.index(C)+1)
