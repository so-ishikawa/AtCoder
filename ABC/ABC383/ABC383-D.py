import math
N = int(input())

def get_prime(num):
    target = set(range(2, num))
    limit = int(math.sqrt(num))
    for i in range(2, limit):
        temp = set(range(i*i, num, i))
        target -= temp
    ans = list(target)
    ans.sort()
    return(ans)

print(get_prime(N))
"""
count_set = set()

prime_list = get_prime(N)
for i in range(len(prime_list)-1):
    for j in range(i+1, len(prime_list)):
        if prime_list[i]*prime_list[j] <= math.sqrt(N):
            count_set.add((i, j))

count = 0
for i in range(2, 20):
    if i**8 <= N:
        count += 1

print(len(count_set) + count)
""" 
