N = int(input())
# A_list = []
# B_list = []
result = [0]*N


for i in range(N):
    a, b = map(int, input().split())
    ans = a*(10**100000000)/(a + b)
    result[i] = (ans, i)
    
result.sort(key=lambda x: (-x[0], x[1]))

for i in range(N):
    print(result[i][1], end=" ")
