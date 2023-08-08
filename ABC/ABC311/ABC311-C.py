N = int(input())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

flag_list = [False]*(N+1)

temp = 1
end_node = -1
for _ in range(len(A_list)):
    if flag_list[temp]:
        end_node = temp
        break
    flag_list[temp] = True
    temp = A_list[temp]

result = []
temp = end_node
for _ in range(len(A_list)):
    if A_list[temp] == end_node:
        result.append(temp)
        break
    result.append(temp)
    temp = A_list[temp]

print(len(result))
for i in result:
    print(i, end=" ")
