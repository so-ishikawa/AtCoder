S = input()
Q = int(input())
K_list = list(map(int, input().split()))

def f(k):
    if k % len(S) == 0:
        n = k // len(S)
        count = 0
        while n != 1:
            count += 1
            n = n // 2
        if count % 2 == 0:
            print(S[-1], end=" ")
            return
        print(S[-1].swapcase(), end=" ")
    else:
        N = k // len(S) + 1
        L = 1
        count = 1
        while not (L > N):
            L *= 2
        # print(N, L)
        # exit()
        while N > 1:
            N = N - L //2
            L = L // 2
            count += 1
        if count % 2 == 0:
            print(S[k%len(S)-1], end=" ")
            return
        print(S[k%len(S)-1].swapcase(), end=" ")


for k in K_list:
    f(k)
