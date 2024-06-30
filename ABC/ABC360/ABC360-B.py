S, T = map(str, input().split())
for w in range(1, len(S)):
    for c in range(1, w+1):
        if c > w:
            break
        
        result = []
        for i in range(w, len(S)+w, w):
            if S[i-w:i] != "":
                result.append(S[i-w:i])

        if len(result) < len(T):
            continue
        flag = True

        for index in range(len(T)):
            # print(result, c, index)
            if len(result[index]) < c-1:
                flag = False
                break
            if result[index][c-1] != T[index]:
                flag = False
                break
        if flag:
            print("Yes")
            exit()
print("No")

