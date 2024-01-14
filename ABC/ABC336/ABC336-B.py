N = int(input())
count = 0
# print(str(bin(N))[-1])
for i in range(len(str(bin(N)))-1, -1, -1):
    if (str(bin(N)))[i] == "0":
        count += 1
        continue
    else:
        break
print(count)
