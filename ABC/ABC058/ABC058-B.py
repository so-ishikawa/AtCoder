O = input()
E = input()

for i in range(len(O)):
    print(O[i], end="")
    if i == len(O)-1 and len(O) != len(E):
        break
    print(E[i], end="")
