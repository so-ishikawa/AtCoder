N, Q = map(int, input().split())

follow_set = set()

for i in range(Q):
    T, A, B = map(int, input().split())

    if T == 1:
        follow_set.add((A, B))
    elif T == 2:
        follow_set.discard((A, B))
    else:
        if (A, B) in follow_set and (B, A) in follow_set:
            print("Yes")
        else:
            print("No")

