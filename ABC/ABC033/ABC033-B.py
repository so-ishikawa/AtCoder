N = int(input())
max_name = ""
max_value = 0
p_list = []
for _ in range(N):
    s, p = map(str, input().split())
    p = int(p)
    if max_value < p:
        max_value = p
        max_name = s
    p_list.append(p)

p_list.sort(reverse=True)
if p_list[0] > sum(p_list)/2:
    print(max_name)
    exit()
print("atcoder")
