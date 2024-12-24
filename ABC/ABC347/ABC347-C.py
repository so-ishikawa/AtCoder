N, A, B = map(int, input().split())
D_list = list(map(int, input().split()))

temp = list()
for i in D_list:
    d = i % (A + B)
    temp.append(d)
print("Yes" if A >= max(temp)-min(temp) else "No")

