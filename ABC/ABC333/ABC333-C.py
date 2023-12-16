import itertools

N = int(input())
seq = []
for i in range(1, 13):
    seq.append(int("1"*i))

temp = list(itertools.combinations_with_replacement(seq, 3))
temp2 = [sum(x) for x in temp]
temp2.sort()
print(temp2[N-1])
# print(len(temp2))
