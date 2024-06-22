N = int(input())
AC_list = []
for i in range(N):
    A, C = map(int, input().split())
    AC_list.append((A, C, i+1))

AC_list.sort(key=lambda x: x[0], reverse=True)

temp = [AC_list[0][2]]

max_c = AC_list[0][1]

for i in AC_list:
    if i[1] < max_c:
        temp.append(i[2])
        max_c = i[1]

print(len(temp))
temp.sort()
print(*temp)

def f():
    aaa

