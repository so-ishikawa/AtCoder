S = input()

max_length = 1
for start in range(0, len(S)):
    for end in range(start+1, len(S)+1):
        target = S[start:end]
        pre = target[:len(target)//2]
        aft = target[-(len(target)//2):]
        aft = aft[::-1]
        if pre == aft and len(target) > max_length:
            max_length = len(target)
print(max_length)
