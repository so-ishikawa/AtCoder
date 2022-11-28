"""
方針
問題を計算すると

N = (A/2B)**(2/3) - 1
でN回操作するのが最適だと分かる　そのNを

t = B*N + A/((N+1)**(1/2))
に入れて回答

Nが小数なので前後+-5 位出して それでtを求めて最小の物を
採用すればよい


"""
import math

a, b = map(int, input().split())
N = (a / (2*b))**(2/3) - 1
N = math.floor(N)

min_value = 99999999999999999999999999999999
for i in range(max(N-5, 0), N+5):
    temp = float(b * i) + float(a) / float((i+1)**(1/2))
    # print('{:.10f}'.format(float(a)/float((i+1)**(1/2))))
    if min_value > temp:
        min_value = temp
print('{:.20f}'.format(min_value))
