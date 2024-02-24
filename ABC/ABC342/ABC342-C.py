N = int(input())
S = input()
Q = int(input())




no_appear_set = set("abcdefghijklmnopqrstuvwxyz")
vanished_set = set({})
dic = dict({"a":None,"b":None,"c":None,"d":None,"e":None,"f":None,"g":None,"h":None,"i":None,"j":None,"k":None,"l":None,"m":None,"n":None,"o":None
,"p":None,"q":None,"r":None,"s":None,"t":None,"u":None,"v":None,"w":None,"x":None,"y":None,"z":None})

for _ in range(Q):
    c, d = map(str, input().split())
    if c in no_appear_set:
        no_appear_set.discard(c)
    """
    if c not in vanished_set:
        vanished_set.add(c)
    if d in vanished_set:
        vanished_set.discard(d)
    """
    # if dic[c] is not None:
    #     continue
    dic[c] = d
    if dic[d] is not None:
        dic[d] = None

S_list = list(S)

for num in range(len(S_list)):
    s = S_list[num]
    if s in no_appear_set:
        continue
    # if s in vanished_set:
    #     continue
    temp = s
    while dic[temp] is not None:
        temp = dic[temp]
    S_list[num] = temp

# print(dic)
print("".join(S_list ))

