# from collections import defaultdict
# from typing import List


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
        return self._root(self.parent[x])


    def issame(self, lhs, rhs):
        """
        lhs, rhsが同じグループに所属するか調べる
        """
        return(self._root(lhs) == self._root(rhs))


    def unite(self, lhs, rhs):
        """
        lhsを含むグループとrhsを含むグループを統合する
        """
        self.parent[rhs] = lhs


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
