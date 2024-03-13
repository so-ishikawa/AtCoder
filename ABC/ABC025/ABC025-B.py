N, A, B = map(int, input().split())
current_position = 0
for _ in range(N):
    s, d = map(str, input().split())
    d = int(d)
    if d < A:
        d = A
    elif B < d:
        d = B
    if s == "East":
        current_position += d
    else:
        current_position -= d

if current_position == 0:
    print(0)
    exit()

if current_position > 0:
    print("East", current_position)
    exit()

print("West", abs(current_position))
