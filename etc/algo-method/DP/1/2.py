N = int(input())
a_list = list(map(int, input().split()))

memo = {}
best_time = 9099990

def func(index, sum_time):

    global a_list
    global memo
    global best_time
    global N


    if index in memo and sum_time > memo[index]:
        return
    else:
        memo[index] = sum_time

    # if index > N-1:
    #    return
    if index == N-1:
        if sum_time < best_time:
            best_time = sum_time
        return

    if N > index+1:
        func(index + 1, sum_time + a_list[index+1])
    if N > index+2:
        func(index + 2, sum_time + 2*a_list[index+2])

func(0, 0)
print(best_time)

