N, X = map(int, input().split())
m_list = []
for _ in range(N):
    m_list.append(int(input()))

print(len(m_list) + (X - sum(m_list) ) // min(m_list))
