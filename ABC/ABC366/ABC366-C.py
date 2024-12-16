Q = int(input())
dic = dict()

ans = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        if query[0] == 1:
            if query[1] in dic:
                if dic[query[1]] == 0:
                    ans += 1
                dic[query[1]] = dic[query[1]] + 1
            else:
                dic[query[1]] = 1
                ans += 1
            continue
            
        #2
        dic[query[1]] = dic[query[1]] - 1
        if dic[query[1]] == 0:
            ans -= 1
        continue
    # 3
    # temp = list(dic.values())
    # print(len(temp)-temp.count(0))
    print(ans)
    continue
