A, B = map(int, input().split())
if 1 not in [A, B]:
    if A > B:
        print("Alice")
        exit()
    if A < B:
        print("Bob")
        exit()
    if A == B:
        print("Draw")
        exit()

#A,B include 1
if A == 1 and B == 1:
    print("Draw")
    exit()

if A == 1:
    print("Alice")
    exit()

# B == 1
print("Bob")
exit()
    
