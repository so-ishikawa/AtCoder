A, B, C = map(int, input().split())
temp = [A, B, C]
min_value = min(temp)
temp.remove(min_value)
print(sum(temp))
