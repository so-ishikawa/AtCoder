N = int(input())
target_list = list(range(1, N+1, 2))
result_list = []

for number in target_list:
    counter = 0
    for i in range(1, number+1):
        if number % i == 0:
            counter = counter + 1
    if counter == 8:
        result_list.append(number)

print(len(result_list))
