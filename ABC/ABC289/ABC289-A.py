"""
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))

"""
s = input()
# print(s)
result = []
for i in range(len(s)):
    # print(i)
    if s[i] == "0":
        result.append("1")
    else:
        result.append("0")
print("".join(result))
