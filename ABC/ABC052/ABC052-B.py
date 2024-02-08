N = int(input())
S = input()

count = 0
max_value = 0

for i in range(N):
    if S[i] == "I":
        count += 1
    if S[i] == "D":
        count -= 1
    if max_value < count:
        max_value = count
print(max_value)
