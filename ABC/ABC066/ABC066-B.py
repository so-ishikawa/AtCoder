S = input()
if len(S) % 2 == 0:
    for i in range(2, len(S), 2):
        temp = S[:(-1)*i]
        if temp[:len(temp)//2] == temp[len(temp)//2:]:
            print(len(temp))
else:
    pass
    """
    S = S[:-1]
    for i in range(0, len(S), 2):
        if i != 0:
            temp = S[:(-1)*i]
        else:
            temp = S
        if temp[:len(temp)//2] == temp[len(temp)//2:]:
            print(len(temp))    
    """
