N = int(input())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

st_list = ["dummy"]
for _ in range(N-1):
    s, t = map(int, input().split())
    st_list.append((s,t))


for i in range(1, N):
    s, t = st_list[i]
    if A_list[i] < s:
        continue
    num = A_list[i] // s
    A_list[i+1] = A_list[i+1] + t*num
# print(A_list)
print(A_list[-1])
