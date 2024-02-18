a, b, X = map(int, input().split())
print(len([x for x in range(a, b+1) if x % X == 0]))
