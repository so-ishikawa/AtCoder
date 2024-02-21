Sa = list(input())
Sb = list(input())
Sc = list(input())

dic = {"a":Sa, "b":Sb, "c":Sc}
current = "a"
while True:
    if len(dic[current]) == 0:
        print(current.upper())
        exit()
    current = dic[current].pop(0)

