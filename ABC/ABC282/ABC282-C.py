N = int(input())
S = input()

top_is_keyword_flag = True

S_split = S.split("\"")
# print(S_split)
if S_split[0] != "":
    top_is_keyword_flag = False

for i in range(len(S_split)):
    if top_is_keyword_flag:
        if i % 2 == 1:
            S_split[i] = S_split[i].replace(",", ".")
    else:
        if i % 2 == 0:
            S_split[i] = S_split[i].replace(",", ".")

print(S_split)
result = ""
for i in S_split:
    if i == "":
        result += "\""
    result = result + "\"" + i

# result = "\"".join(S_split)
# if len(result) != N:
#     result = "\"" + result + "\""
print(result)
