N, M = map(int, input().split())
ab_list = []

koma_position_set = set()
kiki_position_set = set()

for _ in range(M):
    a, b = map(int, input().split())
    ab_list.append((a, b))
    koma_position_set.add((a, b))

for ab in ab_list:
    a = ab[0]
    b = ab[1]
    if a + 2 <= N and b + 1 <= N:
        kiki_position_set.add((a+2,b+1))
    if a + 1 <= N and b + 2 <= N:
        kiki_position_set.add((a+1,b+2))
    if a - 1 >= 1 and b + 2 <= N:
        kiki_position_set.add((a-1,b+2))
    if a - 2 >= 1 and b + 1 <= N:
        kiki_position_set.add((a-2,b+1))
    if a - 2 >= 1 and b - 1 >= 1:
        kiki_position_set.add((a-2,b-1))
    if a - 1 >= 1 and b - 2 >= 1:
        kiki_position_set.add((a-1,b-2))
    if a + 1 <= N and b - 2 >= 1:
        kiki_position_set.add((a+1,b-2))
    if a + 2 <= N and b - 1 >= 1:
        kiki_position_set.add((a+2,b-1))
# print(koma_position_set)
# print(kiki_position_set)
print(N*N-len(kiki_position_set | koma_position_set))
