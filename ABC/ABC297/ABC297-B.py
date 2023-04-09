"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
import re
S = input()

temp = [m.span() for m in re.finditer('B', S)]
if ((temp[0][0]+1) + (temp[1][0]+1)) % 2 != 1:
    # print(temp[0][0]+1)
    print("No")
    exit()

temp2 = [m.span() for m in re.finditer('R', S)]
k = S.find("K")

if not ((temp2[0][0]+1) < (k+1) and (k+1) < (temp2[1][0]+1)):
    print("No")
    exit()
print("Yes")
