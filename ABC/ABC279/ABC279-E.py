N, M = map(int, input().split())
a_list = list(map(int, input().split()))

for i in range(1,M-1):
    temp = [i for i in range(1, N+1)]
    for j in range(1,M-1):
        if i == j:
            continue
        a = temp[j]
        temp[j] = temp[j+1]
        temp[j+1] = a
        print(temp.index(1) +1)

# ‰ğà‚ğ“Ç‚ñ‚¾‚ªè‚ªo‚¸
