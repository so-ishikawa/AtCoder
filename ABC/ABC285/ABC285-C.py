# 1桁 1-27
# 2桁

S = input()
_sum = 0
for i in range(len(S)):
    # print(i, S[i])
    _sum = _sum +  (26**(len(S)-i-1)) * (ord(S[i])-64)
print(_sum)
