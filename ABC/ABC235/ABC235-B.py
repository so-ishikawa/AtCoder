N = int(input())
H_list = list(map(int, input().split()))

ch = H_list[0]
for i in range(1, len(H_list)):
    if H_list[i] > ch:
        ch = H_list[i]
        continue
    print(ch)
    exit()

print(H_list[-1])
exit()
