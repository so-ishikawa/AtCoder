S = input()

start_count = 0
start_index = 0
end_count = 0
end_index = len(S)-1

for i in range(len(S)):
    if S[i] != "a":
        start_index = i
        break
    else:
        start_count += 1

for i in range(len(S)-1, -1, -1):
    if S[i] != "a":
        end_index = i
        break
    else:
        end_count += 1

if start_count > end_count:
    print("No")
    exit()

while True:        
    if S[start_index] != S[end_index]:
        print("No")
        exit()
    start_index += 1
    end_index -= 1
    
    if start_index >= end_index:
        break
print("Yes")
