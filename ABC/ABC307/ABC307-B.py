N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        target = S_list[i] + S_list[j]
        pre = target[:len(target)//2]
        aft = target[-1*(len(target)//2):]
        # print(len(aft))
        aft = aft[::-1]
        # print(len(pre), len(aft))
        if pre == aft:
            print("Yes")
            exit()
print("No")
