N = int(input())
W_list = []
for _ in range(N):
    W_list.append(input())

if N != len(set(W_list)):
    print("No")
    exit()

suf_word = ""
for i in range(len(W_list)):
    if i != 0:
        if W_list[i][0] != suf_word:

            print("No")
            exit()
    suf_word = W_list[i][-1]
print("Yes")
