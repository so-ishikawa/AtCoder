N = input()

temp = 0
for i in range(len(N)):
    if N[i] == "0":
        temp += 1
        continue
    break
# print(N[temp:])
N = N[temp:]

temp = 0
for i in range(len(N)-1,-1, -1):
    if N[i] == "0":
        temp += 1
        continue
    break
# print(temp)
if temp != 0:
    N = N[:-temp]

if N == N[::-1]:
    print("Yes")
    exit()

print("No")
