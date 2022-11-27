import itertools
import math

n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))


seq = [x for x in range(1, n+1)]
l = list(itertools.permutations(seq))
p_index = l.index(tuple(p_list))+1
q_index = l.index(tuple(q_list))+1

print(abs(p_index-q_index))
