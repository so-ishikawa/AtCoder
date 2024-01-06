N = int(input())
# print("hello!")
for x in range(N+1):
    for y in range(N+1):
        if x + y > N:
            continue
        for z in range(N+1):
            if x + y + z > N:
                continue
            print(x, y, z)
