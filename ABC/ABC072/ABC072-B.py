s = input()

for i in range(len(s)):
    if (i + 1) % 2 == 1:
        print(s[i], end="")
