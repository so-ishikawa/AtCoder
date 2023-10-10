N = int(input())
S = input()

if N == 26 or N == 0:
    print(S)
    exit()

aaa = [""]*len(S)

dic = dict()
dic_r = dict()

for i in range(26):
    dic[chr(ord("A") + i)] = i+1
    dic_r[i+1] = chr(ord("A")+i)


def f(char, n):
    if dic[char] + n <= 26:
        return(dic_r[dic[char]+n])
    return(dic_r[(dic[char] + n) % 26])

temp = ""
for i in range(len(S)):
    s = S[i]
    aaa[i] = f(s, N)
    # temp += f(i, N)
print("".join(aaa))
