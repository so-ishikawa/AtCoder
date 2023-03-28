N = int(input())
cent = int(N / 100)
if N % 100 != 0:
    cent += 1
print(cent)
