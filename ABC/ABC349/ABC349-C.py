S = input()
T = input()

length = 3
if T[-1] == "X":
    length = 2

searched = 0
for i in range(length):
    target_char = T[i].lower()
    result = S.find(target_char, searched)
    if result == -1:
        print("No")
        exit()
    searched = result + 1

print("Yes")
