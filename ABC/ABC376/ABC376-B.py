N, Q = map(int, input().split())
L = 1
R = 2
count = 0
for i in range(Q):
    H, T = map(str, input().split())
    T = int(T)
    current_hand_position = R if H == "R" else L
    other_hand_position = L if H == "R" else R
    
    if not (max(current_hand_position, T) > other_hand_position > min(current_hand_position, T)):
        count += (max(current_hand_position, T)-min(current_hand_position, T))
        if H == "R":
            R = T
        else:
            L = T
        continue
    count += (min(current_hand_position, T)+N - max(current_hand_position, T))
    if H == "R":
        R = T
    else:
        L = T

print(count)
