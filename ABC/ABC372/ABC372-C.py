N, Q = map(int, input().split())
S = input()
num = S.count("ABC")

s = list("_" + S)



for _ in range(Q):
    index, char = map(str, input().split())
    index = int(index)

    # no change
    if s[index] == char:
        print(num)
        continue

    if index + 2 <= len(s) - 1 and s[index+2] == "C" and s[index+1] == "B":
        if s[index] == "A":
            num -= 1
        elif char == "A":
            num += 1
    if index + 1 <= len(s) - 1 and s[index+1] == "C" and index -1 >= 0 and s[index-1] == "A":
        if s[index] == "B":
            num -= 1
        elif char == "B":
            num += 1
    if index - 2 >= 0 and s[index-2] == "A" and s[index-1] == "B":
        if s[index] == "C":
            num -= 1
        elif char == "C":
            num += 1

    s[index] = char
    print(num)

        
