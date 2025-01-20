N, T = map(str, input().split())
N = int(N)

result = []

for i in range(N):
    S = input()
    if len(S) == len(T):
        if S == T:
            result.append(i+1)
            continue
        diff_count = 0
        for j in range(len(T)):
            if S[j] != T[j]:
                diff_count += 1
        if diff_count == 1:
            result.append(i+1)
        continue
    # > <
    if abs(len(S)-len(T)) != 1:
        continue

    long_side, short_side = (max(T, S, key=len), min(T, S, key=len))

    short_side = list(short_side)
    diff_count = 0
    for j in range(len(long_side)):
        if j == len(long_side)-1 and diff_count == 0:
            diff_count += 1
            break
        if long_side[j] != short_side[j]:
            if diff_count != 0:
                diff_count += 1
                break
            short_side.insert(j, "_")
            diff_count += 1
    if diff_count == 1:
        result.append(i+1)

print(len(result))
print(*result)
