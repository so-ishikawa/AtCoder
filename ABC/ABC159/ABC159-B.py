S = input()

def check_kaibun(s):
    if len(s) == 1:
        return(True)
    a = s[:len(s)//2]
    b = s[-(len(s)//2):]
    b = b[::-1]
    print(a, b, "?")
    if a != b:
        return(False)
    return(True)

if not check_kaibun(S):
    print("No1")
    exit()

if not check_kaibun(S[:len(S)//2]):
    print(S[:len(S)//2],"!")
    print("No2")
    exit()

if not check_kaibun(S[-(len(S)//2):]):
    print("No3")
    exit()

print("Yes")
exit()


