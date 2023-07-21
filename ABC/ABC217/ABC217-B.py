S1 = input()
S2 = input()
S3 = input()

s_set = set({S1,S2,S3})
all_set = set({"ABC","ARC","AGC","AHC"})

print(list(all_set-s_set)[0])
