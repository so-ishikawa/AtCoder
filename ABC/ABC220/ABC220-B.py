K = int(input())
A, B = map(int, input().split())

def f(target, base):
    digit = len(str(target))
    result = 0
    for i in range(digit):
        result = result + (target // 10**i % 10) * (base**i)
    return(result)

print(f(A, K)*f(B, K))
