N = int(input())
S = input()

def f(char_num, diff):
    return((char_num - 64 + diff) % 27)

def a(s, n):
    return(chr(f(ord(s), n) + 64))

temp = ""
for i in S:
    temp += a(i, N)

print(temp)
