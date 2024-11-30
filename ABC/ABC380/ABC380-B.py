S = input()
result = S.split("|")
result = [x for x in result if x != '']

for i in result:
    print(len(i), end=" ")
