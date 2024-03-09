n, m = map(int, input().split())
long_degree = (n % 12) * 30 + m * 0.5
short_degree = 6 * m

k = int(abs(long_degree - short_degree))
print(min(k, 360-k))
