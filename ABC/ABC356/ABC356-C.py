N, M, K = map(int, input().split())
C, A, R = [],[],[]
for _ in range(M):
    CAR = list(input().split())
    C.append(int(CAR[0]))
    A.append(list(map(int, CAR[1:-1])))
    R.append(CAR[-1])

for key_state in range(1 << N):
    for m in range(M):
        for test_case_each_value in A[m]:
            temp = (key_state >> (test_case_each_value - 1))
            temp & 1
