S = input()
N = int(input())

for _ in range(N):
    l, r = map(int, input().split())
    temp = S[l-1:r]
    # print(temp)
    temp = temp[::-1]
    # print(temp)
    S = S[:l-1] + temp + S[r:]

print(S)
