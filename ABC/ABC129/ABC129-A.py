P, Q, R = map(int, input().split())
temp = list([P, Q, R])
temp.remove(max(temp))
print(sum(temp))
