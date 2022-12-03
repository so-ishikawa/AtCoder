k = int(input())

def prime_factorize(N):
    # 答えを表す可変長配列
    res = []

    # √N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p

        # 答えに追加
        res.append((p, e))

    # 素数が最後に残ることがありうる
    if N != 1:
        res.append((N, 1))

    return res

# 460 を素因数分解する
N = k
pf = prime_factorize(N)

x = pf[len(pf)-1][0]
if math.factorial(x) < k:
    




"""
import math
N = 280
result = []

def yaku(n):
    aaa = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if N % i == 0:
            aaa.append(i)
            aaa.append(int(n/i))
    aaa.sort()
    return aaa

temp = yaku(N)
for i in temp:
    bbb = yaku(i)
    result += bbb


result.sort()
cc = int(len(result)/2)
if cc == 1:
    print(N)
else:
    print(cc)
"""
