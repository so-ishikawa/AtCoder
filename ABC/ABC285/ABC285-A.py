a,b = map(int, input().split())
"""
if a * 2 == b or a * 2 == b+1:
    print("Yes")
else:
    print("No")
"""
dic = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12,13],7:[14,15],8:[4],9:[4],10:[5],11:[5],12:[6],13:[6],14:[7],15:[7]}

if b in dic[a]:
    print("Yes")
else:
    print("No")
