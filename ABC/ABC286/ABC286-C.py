N, A, B = map(int, input().split())
S = input()

min_cost = 9999999999999999999999999999
for i in range(len(S)):
    s = S[i:len(S)]+S[0:i]

    diff_count = 0
    for j in range(len(s)//2):
        if s[j] != s[-1*(j+1)]:
            diff_count += 1
    min_cost = min(min_cost, i*A+diff_count*B)
print(min_cost)
