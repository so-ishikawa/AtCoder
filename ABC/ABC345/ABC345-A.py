S = input()
if not (S[0] == "<" and S[-1] == ">"):
    print("No")
    exit()
    
if S.count("=") == len(S)-2:
    print("Yes")
    exit()

print("No")
