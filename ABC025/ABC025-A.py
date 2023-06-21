import itertools
S = input()
N = int(input())

temp = list(itertools.product(list(S), list(S)))[N-1]
print(temp[0]+temp[1])
