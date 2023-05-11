S = input()
if len(set(S)) == 4:
    print("Good")
    exit()

if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
    exit()

print("Good")
