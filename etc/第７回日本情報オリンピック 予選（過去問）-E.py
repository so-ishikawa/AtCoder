import math

"""
方針

#流れ
1. a_listの情報を縦の並びに持ち変える
2. 横軸のR本を回転させる or notで 全列挙する
3. 2.の際　縦軸毎の評価を行い　合計値を出す
4. 3.最大値が答えとなる

bit演算にて高速かつシンプルに実装する

010100111
111001001
101010101
000011010
111111000

を [01101, 11001, 01101, 10001, 00111, 01011, 10100, 10010, 11100]
として管理する

R個のどの横軸を動かす or 動かさないを全てのパターン考える
その際bitで0(全く動かさない), 1(最初の横軸のみ動かす), 2(2番目のみ),3(1,2番目)..
の要領で計算すると簡潔そう

01の文字列をbit列として解釈
int("0110", 2)

3の評価について
0010100
ではRが7　で表が2 裏が5だが　これは裏返すことを考えて5と評価する
1111001
ではRが7　で表が5　裏が2で　裏返さないとして5と評価する

0 裏返して 7
1 裏返して 6
2 裏返して 5
3 裏返して 4
4 そのまま 4
5 そのまま 5
6 そのまま 6
7 そのまま 7

value if value > R//2 else R - value で評価

"""
# """
R, C = map(int, input().split())
a_list = []
for i in range(R):
    temp = list(map(int, input().split()))
    a_list.append(temp)
# """

# 非常に高速な1の数え上げbit演算
# https://yottagin.com/?p=2808
def count_ones_by_shift_2(num):
    num = (num & 0x55555555) + (num >> 1 & 0x55555555)
    num = (num & 0x33333333) + (num >> 2 & 0x33333333)
    num = (num & 0x0F0F0F0F) + (num >> 4 & 0x0F0F0F0F)
    num = (num & 0x00FF00FF) + (num >> 8 & 0x00FF00FF)
    num = (num & 0x0000FFFF) + (num >>16 & 0x0000FFFF)
    return num


# 右からN桁目を反転させる
# 一番右が0桁目 次が1桁目...
# https://yottagin.com/?p=5261
def toggle_nth_bit(num: int, n: int):
    return num ^ (1 << n)


# 左からN桁目を反転させる
# 一番左が0桁目 次が1桁目
def toggle_nth_bit_r(num: int, n: int):
    digit = math.ceil(math.log2(num))
    if digit - n - 1 <= 0:
        return 0
    return num ^ (1 << (digit - n - 1))


# 全M桁の左からN桁目を反転させる
def toggle_nth_bit_rr(num: int, n: int, m: int):
    return(toggle_nth_bit(num, m - n - 1))


# 右からN桁目が1ならTrue 0ならFalse
# 一番右が0桁目 次が1桁目
def is_flag_on(num: int, n: int):
    return True if num & 2 ** n else False

# 左からN桁目が1ならTrue 0ならFalse
# 一番左が0桁目　次が1桁目
def is_flag_on_r(num: int, n:int):
    digit = math.ceil(math.log2(num))
    return is_flag_on(num, digit - n - 1)

# 全M桁の左からN桁目が1ならTrue 0ならFalse
def is_flag_on_rr(num: int, n: int, m: int):
    return is_flag_on(num, m - n - 1)


# 1. a_listの情報を縦の並びに持ち変える
a_list_v = [""] * C
for index in range(C):
   for i in a_list:
       a_list_v[index] = a_list_v[index] + str(i[index])

a_list_v = [int(x, 2) for x in a_list_v]

# 2. 横軸のR本を回転させる or notで 全列挙する
# 横軸一番上が0 一番したがR-1
# 00000000 から 11111111 でそれぞれの軸のon/offを管理

max_value = 0

for R_state in range(0, int("1"*R, 2)+1):
    temp = a_list_v

    for digit in range(R):
        if is_flag_on_rr(R_state, digit, R):
           temp = [toggle_nth_bit_rr(x, digit, R) for x in temp]
    result = [count_ones_by_shift_2(x) for x in temp]

    for i in range(len(result)):
        result[i] = result[i] if result[i] > R//2 else R - result[i]
    if max_value < sum(result):
        max_value = sum(result)

print(max_value)
# print(bin(10), [count_ones_by_shift_2(x) for x in [10]])
# int(format(3,'b'))
