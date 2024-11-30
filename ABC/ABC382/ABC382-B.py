N, D = map(int, input().split())
S = input()
S_list = list(S)
S_list.reverse()

for i in range(D):
    temp = i
    while True:
        if S_list[temp] == ".":
            temp += 1
            continue
        S_list[temp] = "."
        break

S_list.reverse()
print("".join(S_list))
