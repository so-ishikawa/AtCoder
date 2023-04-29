# A, B = map(int, input().split())
# l = list(map(int, input().split()))
N, A, B = map(int, input().split())
C_list = list(map(int, input().split()))

temp = A + B
print(C_list.index(temp) + 1)
