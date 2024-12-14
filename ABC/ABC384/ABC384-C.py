pattern = ["ABCDE","BCDE","ACDE","ABDE","ABCE","ABCD","CDE","BDE","ADE","BCE","ACE","BCD","ABE","ACD","ABD","ABC","DE","CE","BE","CD","AE","BD","AD","BC","AC","AB","E","D","C","B","A"]

a, b, c, d, e = map(int, input().split())
# score = [a, b, c, d, e]

dic = dict()

for i in pattern:
    temp = 0
    if "A" in i:
        temp += a
    if "B" in i:
        temp += b
    if "C" in i:
        temp += c
    if "D" in i:
        temp += d
    if "E" in i:
        temp += e
    dic[i] = temp
  
list_ = list(dic.items())

list_.sort(key=lambda x: (-x[1], x[0]))

for i in list_:
    print(i[0])
