import re

N = int(input())
S = input()
a =  re.search(r"[(].?[)]", S)
print(a)
# while True:
#     a = re.findall(r"[(].?[)]", S)
#     if a == []:
#         break
#     S = S.replace(a[0], "")
# print(S)
