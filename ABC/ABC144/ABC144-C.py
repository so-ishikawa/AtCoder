def f(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border+1):
        if n%small == 0:
            table.append(small)
            big = n//small
            bigs.append(big)
    if border == sq:
        bigs.pop()
    table += reversed(bigs)
    return table

N = int(input())
result = f(N)

min_score = 99999999999999999999999
for i in range(len(result)//2+1):
    temp = result[i] - 1 + N // result[i] - 1
    if min_score > temp:
        min_score = temp
print(min_score)

