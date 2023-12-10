K, G, M = map(int, input().split())

g_value = 0
m_value = 0

for _ in range(K):
    if g_value == G:
        g_value = 0
        continue
    if m_value == 0:
        m_value = M
        continue
    g_emp = G - g_value
    m_least = m_value
    if g_emp < m_least:
        g_value = G
        m_value = m_value - g_emp
        continue
    g_value = g_value + m_least
    m_value = 0
print(g_value, m_value)
