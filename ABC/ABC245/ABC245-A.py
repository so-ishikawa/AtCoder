A, B, C, D = map(int, input().split())
print("Takahashi" if (A*3600+B*60)<(C*3600+D*60+1) else "Aoki")
