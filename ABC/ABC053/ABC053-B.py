s = input()

A_index = 0
for i in range(len(s)):
    if s[i] == "A":
        A_index = i
        # print(i,"!")
        break

Z_index = 0
for i in range(-1, -1*len(s), -1):
    if s[i] == "Z":
        Z_index = i
        #print(i,"!!")
        break

if Z_index == -1:
    print(len(s[A_index:]))
    exit()
print(len(s[A_index:Z_index+1]))
