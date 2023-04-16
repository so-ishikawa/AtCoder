"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""

from collections import deque

Q = int(input())
# query_list = []
# for i in range(Q):
#     l = list(map(int, input().split()))
#     query_list.append(l)

data = deque([1])
# digit = 1
num = 1
NUMBER = 998244353

# for query in query_list:
for _ in range(Q):
    # query = list(map(int, input().split()))
    query = input().split()
    query_0 = int(query[0])
    if query_0 == 1:
        query_1 = int(query[1])
        num = num * 10 + query_1
        data.append(query_1)
        # digit += 1
        num%=NUMBER

    elif query_0 == 2:
        # num = num - (data[0] * (10**(len(data)-1)))
        num = num - data[0] * pow(10, len(data)-1, NUMBER)
        data.popleft()
        # digit -= 1
        # num%=NUMBER

    else: #3
        print(num%NUMBER)

