"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で受け取るとき
s = input().split()
"""
S = input()
T = input()

for i in range(len(T)+1):
    # print(i)
    s_ = S[0:i] + S[-1*(len(T)-i):len(S)]
    flag = True
    for j in range(len(T)):
        if s_[j] == "?" or T[j] == "?":
            continue
        if s_[j] == T[j]:
            continue
        flag = False
        break
    if flag:
        print("Yes")
    else:
        print("No")
