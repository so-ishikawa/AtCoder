"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
S = input()

first_bar = False
second_bar = False
star = False
result = False

for i in S:
    if i == "|" and first_bar == False:
        first_bar = True
        continue
    if i == "*" and first_bar == True and star == False:
        star = True
        continue
    if i == "|" and first_bar == True and star == True and second_bar == False:
        print("in")
        exit()
print("out")
        
