S = input()

temp = set()
for i in range(1, 350):
    if i == 316:
        continue
    temp.add("ABC" + str(i).zfill(3))

if S in temp:
    print("Yes")
    exit()
print("No")
