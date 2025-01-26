K, N = map(int, input().split())
A_list = list(map(int, input().split()))

diff_list = []
for i in range(len(A_list)):
    if i==len(A_list)-1:
        diff_list.append(K - A_list[-1] + A_list[0])
        break
    diff_list.append(A_list[i+1]-A_list[i])

diff_list.sort()
diff_list.pop()
print(sum(diff_list))
