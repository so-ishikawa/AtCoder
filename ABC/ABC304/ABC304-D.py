import bisect

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


A_list.sort()
B_list.sort()

piece_dict = dict()

result_m = None
result_M = None

for i in st_list:
    x = bisect.bisect(A_list, i[0])
    y = bisect.bisect(B_list, i[1])
    if (x, y) in piece_dict:
        piece_dict[(x, y)] = piece_dict[(x, y)] + 1
        continue
    piece_dict[(x, y)] = 1



vals = piece_dict.values()
result_m = min(vals)
result_M = max(vals)
 
if (A+1)*(B+1) > len(piece_dict):
    result_m = 0

print(result_m, result_M)
