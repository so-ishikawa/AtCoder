H, W, N = map(int, input().split())
AB_list = []
H_list = []
W_list = []
for i in range(N):
    h, w = map(int, input().split())
    AB_list.append((h, w))
    H_list.append(h)
    W_list.append(w)

H_list = list(set(H_list))
H_list.sort()
W_list = list(set(W_list))
W_list.sort()

H_dic = dict()
W_dic = dict()

h_count = 1
for i in H_list:
    H_dic[i] = h_count
    h_count += 1

w_count = 1
for i in W_list:
    W_dic[i] = w_count
    w_count += 1

for i in range(N):
    p = AB_list[i]
    print(H_dic[p[0]], W_dic[p[1]])


