A, B = map(int, input().split())
len_A = len(str(A))
len_B = len(str(B))

length = max(len_A, len_B)

for i in range(length):
    a = (A // (10**i) ) % 10
    b = (B // (10**i) ) % 10
    if a + b >= 10:
        print("Hard")
        exit()
print("Easy")
exit()
