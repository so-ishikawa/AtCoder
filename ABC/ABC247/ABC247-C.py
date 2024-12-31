N = int(input())
def f(n,current_n, s):
    # print(s)
    if n < current_n:
        return(s)
    return(f(n, current_n+1, s+","+str(current_n)+","+s))

temp = f(N,1,"")
print(*list(temp.split(",")))
