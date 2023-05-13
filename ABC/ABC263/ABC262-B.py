N = int(input())
P_list = list(map(int, input().split()))

counter = 0
temp = N

while temp != 1:
    temp = P_list[temp - 2]
    counter += 1

print(counter)
