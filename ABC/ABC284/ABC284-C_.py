# UnionFindで実装
# WAで通らず UnionFind側にバグがある可能性がある　01/11

import sys
sys.setrecursionlimit(10**7)


class UnionFind:

    def __init__(self, num):
        """
        """
        # 配列のindexで親子関係を表現する
        self.parent = [-1] * num


    def _root(self, x):
        """
        xの大本の親を調べる
        """
        if self.parent[x] == -1:
            return(x)
        # 経路圧縮
        self.parent[x] = self._root(self.parent[x])
        return self.parent[x]


    def issame(self, lhs, rhs):
        """
        lhs, rhsが同じグループに所属するか調べる
        """
        return(self._root(lhs) == self._root(rhs))


    def unite(self, lhs, rhs):
        """
        lhsを含むグループとrhsを含むグループを統合する
        """
        # 高速化を考えると根をそれぞれ取って比較した方が良い？
        lhs_root = self._root(lhs)
        rhs_root = self._root(rhs)
        if lhs_root == rhs_root:
            return False
        # if self.issame(lhs, rhs):
        #     return False
        self.parent[rhs] = lhs





N, M = map(int, input().split())
uv_list = []

for i in range(M):
    u, v = map(int, input().split())
    uv_list.append((u,v))

union = UnionFind(N+1)
for i in range(M):
    union.unite(uv_list[i][0], uv_list[i][1])

union.parent.pop(0)
print(union.parent.count(-1))
