from itertools import combinations, chain

n = int(input()) 
A_list = list(map(int, input().split()))
q = int(input())
m_list = list(map(int, input().split()))

result = [*chain(*(combinations(A_list, n+1) for n in range(len(A_list))))]
result = [sum(i) for i in result]
for i in m_list:
    if i in result:
        print("yes")
    else:
        print("no")
