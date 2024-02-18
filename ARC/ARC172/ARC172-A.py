H, W, N = map(int, input().split())
A_list = list(map(int, input().split()))
choco_list = [2**x for x in A_list]
choco_list.sort(reverse=True)

H_capable = [0]*H
W_capable = [0]*W

if sum([x*x for x in choco_list]) > H*W:
    print("No")
    exit()


for choco in choco_list:
    flag = False
    for h in range(H):
        if choco + H_capable[h] > W:
            continue
        for w in range(W):
            if choco + W_capable[w] > H:
                continue
            if h + choco > H or w + choco > W:
                continue
            #ok
            # print("OK:", h, choco, H_capable, W_capable)
            for _h in range(choco):
                H_capable[h+_h] = H_capable[h+_h] + choco
            for _w in range(choco):
                # print(W_capable, w, _w)
                W_capable[w+_w] = W_capable[w+_w] + choco
            flag = True
            break
        if flag:
            break
    if not flag:
        print("No")
        exit()
    # print(H_capable, W_capable)
print("Yes")
