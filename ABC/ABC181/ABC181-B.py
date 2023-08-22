N = int(input())

temp = 0
for i in range(N):
    a, b = map(int, input().split())
    if (b - a + 1) % 2 == 1:
        middle = (b + a)//2
        num = (((b - a + 1) - 1) // 2 )*(a+b)
        temp = temp + middle + num
    else:
        temp = temp +  (((b - a + 1)) // 2 )*(a+b)

print(temp)
