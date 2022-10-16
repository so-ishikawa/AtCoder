import bisect
n = int(input())
a_list = list(map(int, input().split()))

kind_list = list(sorted(set(a_list)))


result = [0] * n

for i in a_list:
    # index = kind_list.index(i)
    index = bisect.bisect_right(kind_list, i)
    # print("i:", i, "index:", index, "len(kind_list):", len(kind_list))
    # result[len(kind_list) - (index+1)] += 1
    result[len(kind_list) - index] += 1

print(*result, sep="\n")
