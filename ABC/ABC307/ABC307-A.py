N = int(input())
A_list = list(map(int, input().split()))
temp = 0
counter = 0
for i in range(len(A_list)):
    counter += 1
    temp += A_list[i]
    if counter == 7:
        print(temp, end=" ")
        temp = 0
        counter = 0
