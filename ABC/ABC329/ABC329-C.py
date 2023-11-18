N = int(input())
S = input()

dic = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,
       "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
       "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

counter = 0
pre_char = "_"

for i in S:
    if i == " ":
        counter = 1
        pre_char = i
        continue

    if pre_char == i:
        counter += 1
        if dic[i] < counter:
            dic[i] = counter
        continue

    counter = 1
    pre_char = i
    if dic[i] == 0:
        dic[i] = 1

print(sum(dic.values()))
    
