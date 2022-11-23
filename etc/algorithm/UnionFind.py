# from collections import defaultdict
# from typing import List

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

# 親子関係を図示しちゃんと効率的な改善が行われているか確認してから進んだ方が良さそう
"""
A
 -B -C
    -D
 -E
"""

a = 1 #index 0
b = 2 #index 1
c = 3 #index 2

uf = UnionFind(3)
uf.unite(0, 1)
print(uf.issame(0,1))
print(uf.issame(1,2))

uf.unite(1,2)
print(uf.issame(1,2))
print(uf.issame(0,2))

