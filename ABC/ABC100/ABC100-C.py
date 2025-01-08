N = int(input())
a_list = list(map(int, input().split()))

def count_two(num):
    return((num ^ (num - 1)).bit_length() - 1)

sum_ = 0
[sum_ := sum_ + count_two(x) for x in a_list]

print(sum_)
