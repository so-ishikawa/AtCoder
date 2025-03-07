from collections import deque

N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
check_set = set()

diff = 10**10

for i in range(len(a_list)):
    if a_list[i] not in check_set:
        check_set.add(a_list[i])
        continue
    a_list[i] = a_list[i] + diff
    diff += 1

a_list.sort()

d = deque(a_list)

book_no = 0
while True:
    if len(d) == 0:
        break

    if book_no+1 == d[0]:
        d.popleft()
        book_no += 1
        continue

    if len(d) < 2:
        break

    d.pop()
    d.pop()

    book_no += 1

print(book_no)
