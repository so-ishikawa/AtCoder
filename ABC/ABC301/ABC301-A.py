# A, B = map(int, input().split())
# l = list(map(int, input().split()))
N = int(input())
S = input()

if S.count("T") > S.count("A"):
    print("T")
    exit()
elif S.count("T") < S.count("A"):
    print("A")
    exit()

if S[-1] == "T":
    print("A")
else:
    print("T")
