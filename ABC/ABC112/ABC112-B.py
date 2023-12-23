N, T = map(int, input().split())
c_t_list = []
for _ in range(N):
    c, t = map(int, input().split())
    c_t_list.append((c,t))

temp = [x for x in c_t_list if x[1] <= T]
if len(temp) == 0:
    print("TLE")
    exit()
temp.sort(key=lambda x: x[0])
print(temp[0][0])
