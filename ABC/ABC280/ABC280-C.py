s = input()
t = input()

for i in range(len(s)):
    if s[i] == t[i] and i != len(s)-1:
        continue
    if i == len(s) - 1:
        if s[i] == t[i]:# last
            print(len(s)+1)
            break
        else:
            print(len(s)) #saigo ikkomae
            break
    print(i+1)
    break


