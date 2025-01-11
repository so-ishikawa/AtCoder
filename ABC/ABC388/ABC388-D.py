N = int(input())
A_list = list(map(int, input().split()))

adult_num = [0]*len(A_list)
life_length = [0]*len(A_list)

for i in range(len(A_list)):
    temp = 1 + A_list[i] + adult_num[max(0,i-1)] + i
    life_length[i] = temp

    for j in range(temp):
        if i+j == len(adult_num):
            break
        adult_num[i+j] += 1

    print(temp, life_length, adult_num)
    # if i == 1:
    #     break
print(*[max(0, x-N) for x in life_length])
