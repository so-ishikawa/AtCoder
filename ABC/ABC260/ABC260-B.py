N, X, Y, Z = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

Score_list = []
for i in range(N):
    Score_list.append([i+1, A_list[i], B_list[i]])

Score_list_sorted_math = sorted(Score_list, key=lambda x:(-x[1],x[0]))
math_ok, math_ng = Score_list_sorted_math[:X], Score_list_sorted_math[X:]

Score_list_sorted_eng = sorted(math_ng, key=lambda x:(-x[2],x[0]))
eng_ok, eng_ng = Score_list_sorted_eng[:Y], Score_list_sorted_eng[Y:]

Score_list_sorted_both = sorted(eng_ng, key=lambda x:(-(x[1]+x[2]),x[0]))
both_ok, _ = Score_list_sorted_both[:Z], Score_list_sorted_both[Z:]

pass_member = math_ok + eng_ok + both_ok
pass_member = sorted(pass_member, key=lambda x:x[0])
for i in pass_member:
    print(i[0])