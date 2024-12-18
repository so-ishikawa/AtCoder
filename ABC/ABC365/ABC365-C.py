N, M = map(int, input().split())
A_list = list(map(int, input().split()))

if sum(A_list) <= M:
    print("infinite")
    exit()

A_list.sort(reverse=True)
cumulative_list_reverse = []
temp = sum(A_list)

for i in A_list:
    temp -= i
    cumulative_list_reverse.append(temp)

for index in range(len(cumulative_list_reverse)):
    i = cumulative_list_reverse[index]
    if M - i <= 0:
        continue
    remain = M - i
        
    if index+1 != len(A_list) and (remain / (index+1)) <= A_list[index+1]:
        continue
    print(remain//(index+1))
    exit()
