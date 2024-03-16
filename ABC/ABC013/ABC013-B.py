a = int(input())
b = int(input())

big = max(a, b)
small = min(a, b)

print(min(big-small, small+10-big))
