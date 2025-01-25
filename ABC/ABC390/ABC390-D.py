import itertools

N = int(input())
A_list = list(map(int, input().split()))

result_set = set()

for i in range(2, len(A_list)+1):
    for index_pair in itertools.combinations(range(len(A_list)), i):
        print(index_pair)
        sum_ = 0
        temp = []
        for j in range(len(A_list)):
            if j in index_pair:
                sum_ += A_list[j]
                continue
            temp.append(A_list[j])
        temp.append(sum_)
        xx = 0
        for k in temp:
            xx = xx ^ k
        result_set.add(xx)
xx = 0
for i in A_list:
    xx = xx ^ i
result_set.add(xx)
print(len(result_set))
