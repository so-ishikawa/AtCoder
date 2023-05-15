N, K = map(int, input().split())
S = input()

temp = list(S)
temp[K-1] = temp[K-1].lower()
print("".join(temp))