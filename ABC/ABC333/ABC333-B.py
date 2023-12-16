s = input()
S1 = s[0]
S2 = s[1]

t = input()
T1 = t[0]
T2 = t[1]

dic = {("A", "B"):1, ("A", "C"):2, ("A", "D"):2, ("A", "E"):1,
       ("B", "C"):1, ("B", "D"):2, ("B", "E"):2, ("C", "D"):1,
       ("C", "E"):2, ("D", "E"):1}

if dic[(min(S1, S2),max(S1, S2))] == dic[(min(T1, T2),max(T1,T2))]:
    print("Yes")
else:
    print("No")
