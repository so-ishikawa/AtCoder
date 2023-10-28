N = int(input())

for i in range(N, 919+1):
    i_ = str(i)
    if int(i_[0])*int(i_[1]) == int(i_[2]):
        print(i)
        exit()
