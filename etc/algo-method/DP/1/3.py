import sys
N = int(input())

if N == 1:
    print(1)
    sys.exit(0)
elif N == 2:
    print(2)
    sys.exit(0)
elif N == 3:
    print(3)
    sys.exit(0)

counter = 0
# counter = 0
def func(floor_no, _N):
    global counter
    if floor_no == _N:
        counter += 1
        return

    if floor_no + 1 <= _N:
        func(floor_no+1, _N)
    if floor_no + 2 <= _N:
        func(floor_no+2, _N)

# func(0,5)
# print(counter)

counter = 0
result = 0
if N % 2 == 0:
    func(0, N/2)
    even_0 = counter * counter
    counter = 0

    func(0, (N - 2)/2)
    even_1 = counter * 1 * counter
    counter = 0
    # print(even_0, even_1)
    result = even_0 + even_1
else:
    func(0, (N-1)/2)
    odd_0 = counter * 1 * counter
    counter = 0


    small = (N-3)/2
    large = (N-3)/2 + 1
    func(0, small)
    small_counter = counter
    counter = 0
    func(0, large)
    large_counter = counter
    counter = 0

    odd_1 = small_counter * 1 *large_counter * 2
    counter = 0

    result = odd_1 + odd_0

print(result)





