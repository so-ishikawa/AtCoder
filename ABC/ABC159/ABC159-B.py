S = input()

def check_kaibun(s):
    if len(s) == 1:
        return(True)
    a = s[:len(s)//2]
    b = s[-(len(s)//2):]
    b = b[::-1]
    if a != b:
        return(False)
    return(True)

if not check_kaibun(S):
    print("No")
    exit()

if not check_kaibun(S[:len(S)//2]):
    print("No")
    exit()

if not check_kaibun(S[-(len(S)//2):]):
    print("No")
    exit()

print("Yes")
exit()


