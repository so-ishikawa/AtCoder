import copy

# l = list(map(int, input().split()))
W, H = map(int, input().split())
N = int(input())
st_list = []
for i in range(N):
    p, q = map(int, input().split())
    st_list.append((p,q))
A = int(input())
A_list = list(map(int, input().split()))
B = int(input())
B_list = list(map(int, input().split()))

waku_list = []
waku_list.append(st_list)
# print(waku_list)
# temp = []
for i in A_list:
    temp = []
    for j in waku_list:
        if len(j) == 0:
            continue
        k = [x for x in j if x[0] >= i]
        temp.append(k)
        k = [x for x in j if x[0] < i]
        temp.append(k)
    waku_list = copy.deepcopy(temp)

for i in B_list:
    temp = []
    for j in waku_list:
        if len(j) == 0:
            continue
        k = [x for x in j if x[1] >= i]
        temp.append(k)
        k = [x for x in j if x[1] < i]
        temp.append(k)
    waku_list = copy.deepcopy(temp)
# print(waku_list)
min_value = 9999999999
max_value = 0
for i in waku_list:
    if len(i) > max_value:
        max_value = len(i)
    if len(i) < min_value:
        min_value = len(i)

print(min_value, max_value)

