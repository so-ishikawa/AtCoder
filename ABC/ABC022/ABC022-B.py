N = int(input())
set_ = set()
for _ in range(N):
    set_.add(int(input()))

print(N-len(set_))
