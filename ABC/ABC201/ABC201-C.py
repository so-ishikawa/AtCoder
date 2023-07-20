S = input()
maru_set = set()
batsu_set = set()

for i in range(len(S)):
    if S[i] == "o":
        maru_set.add(str(i))
        continue
    if S[i] == "x":
        batsu_set.add(str(i))
        continue
    
count = 0
for i in range(10000):
    temp = set(str(i).zfill(4))
    if not (temp >= maru_set):
        continue
    if not temp.isdisjoint(batsu_set):
        continue
    count += 1
print(count)
        
