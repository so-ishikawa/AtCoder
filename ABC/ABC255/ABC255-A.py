R, C = map(int, input().split())
A_11, A_12 = map(int, input().split())
A_21, A_22 = map(int, input().split())

mat = []
for i in range(3):
    temp = [0] * 3
    mat.append(temp)

mat[1][1] = A_11
mat[1][2] = A_12
mat[2][1] = A_21
mat[2][2] = A_22

print(mat[R][C])
