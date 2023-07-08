N = int(input())
s_list = []
t_list = []

for i in range(N):
    s, t = map(str, input().split())
    
    s_list.append(s)
    t_list.append(t)

for i in range(N):
    if s_list[i] == t_list[i]:
        if not (s_list.count(s_list[i]) == 1 and t_list.count(s_list[i]) == 1):
            print("No")
            exit()
        continue
    
    if not ((s_list.count(s_list[i]) == 1 and t_list.count(s_list[i]) == 0) or (s_list.count(t_list[i]) == 0 and t_list.count(t_list[i]) == 1)):
        print("No")
        exit()
print("Yes")
exit()
