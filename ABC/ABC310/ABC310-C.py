N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

a = list(set(S_list))
# a_size = len(a)
b = [x for x in a if x != x[::-1]]
b_size = len(b)

temp = set(b)
for i in b:
    temp.add(i[::-1])

print(b_size - ((2*b_size - len(temp))//2) + (len(a)-b_size))
