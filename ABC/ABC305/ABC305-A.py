
# l = list(map(int, input().split()))

N = int(input())
temp = (N // 5) * 5
if N - temp > 2.5:
    print(temp+5)
else:
    print(temp)
