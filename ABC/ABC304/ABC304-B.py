# l = list(map(int, input().split()))
import math
N = int(input())

if N <= 10**3 - 1:
    print(N)
    exit()

if N >= 10**3 and N <= 10**4 - 1:
    print(math.floor(N/10)*10)
    exit()

if N >= 10**4 and N <= 10**5 - 1:
    print(math.floor(N/100)*100)
    exit()

if N >= 10**5 and N <= 10**6 - 1:
    print(math.floor(N/1000)*1000)
    exit()

if N >= 10**6 and N <= 10**7 - 1:
    print(math.floor(N/10000)*10000)
    exit()

if N >= 10**7 and N <= 10**8 - 1:
    print(math.floor(N/100000)*100000)
    exit()

if N >= 10**8 and N <= 10**9 - 1:
    print(math.floor(N/1000000)*1000000)
    exit()
