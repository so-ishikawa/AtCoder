N = int(input())
p_list = list(map(int, input().split()))

result = [None] * (N+1)
for i in range(1, len(p_list)+1):
    index = p_list[i-1]
    result[index] = i

result.pop(0)
print(*result)
