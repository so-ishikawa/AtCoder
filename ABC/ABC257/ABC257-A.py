N, X = map(int, input().split())
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp = []
for i in chars:
    temp.append(i * N)

result = "".join(temp)
print(result[X-1])


# char_num = X // N - 1
# print(chars[char_num])
