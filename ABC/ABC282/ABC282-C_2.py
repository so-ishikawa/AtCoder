# 別解
# 当初この方法を思いついたが方向性が良くないかと断念
# 解答を見たところ方針自体は間違っていないことを確認したので試しに実装


N = int(input())
S = input()

sep = S.split("\"")
for i in range(len(sep)):
    if i % 2 != 0:
        continue
    sep[i] = sep[i].replace(",", ".")
print("\"".join(sep))
