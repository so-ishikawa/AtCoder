N = int(input())
S = input()

flag = False #out of " " is False
out_list = []
for i in range(len(S)):
    if S[i] == "\"":
        flag = not flag
    if flag is False and S[i] == ",":
        out_list.append(".")
    else:
        out_list.append(S[i])
print("".join(out_list))
