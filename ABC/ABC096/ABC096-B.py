A, B, C = map(int, input().split())
K = int(input())

temp = [A, B, C]
temp.sort()
print(temp[-1]*(2**K) + temp[0] + temp[1])

