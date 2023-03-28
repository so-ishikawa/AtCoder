S = input()
T = input()

if len(S) > len(T):
   print("No")
   exit()

if len(S) == 0 and len(T) >= 0:
    print("Yes")
    exit()

if T[:len(S)] == S:
    print("Yes")
    exit()

print("No")
