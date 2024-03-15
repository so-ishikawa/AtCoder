X = input()

h_flag = False

for i in X:
    if i == "h" and h_flag:
        h_flag = False
        continue
    if h_flag:
        print("NO")
        exit()
    if i == "c":
        h_flag = True
        continue
    if i == "o":
        continue
    if i == "k":
        continue
    if i == "u":
        continue
    print("NO")
    exit()

if h_flag:
    print("NO")
    exit()

print("YES")
    
