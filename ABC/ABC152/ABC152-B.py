a, b = map(int, input().split())
temp = [str(a)*b, str(b)*a]
temp.sort()

print(temp[0])
