A, B, C = map(int, input().split())
temp = sorted([A, B, C], reverse=True)

print(temp[0]*10 + temp[1] + temp[2])
