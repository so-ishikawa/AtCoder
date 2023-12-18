N = int(input())
p_list = []
for _ in range(N):
    p_list.append(int(input()))

p_list.sort()

print(int(sum(p_list[:-1]) + p_list[-1]//2))
