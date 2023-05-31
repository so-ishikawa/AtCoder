A1, A2, A3 = map(int, input().split())

temp = [A1, A2, A3]
temp.sort()

print(abs(temp[1]-temp[0])+abs(temp[2]-temp[1]))

