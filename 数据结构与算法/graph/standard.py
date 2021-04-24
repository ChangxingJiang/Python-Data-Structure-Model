# -*-coding:GBK -*-

"""
ͼ
"""

from copy import deepcopy
from typing import Dict
from typing import Tuple

from .base import BaseEdge
from .base import BaseGraph
from .base import BaseVertex


class Graph(BaseGraph):
    """ͼ"""

    class Vertex(BaseVertex):
        """�������Ľڵ����"""

        def __init__(self, x):
            self._element = x

        def element(self):
            """���ؽڵ��ֵ"""
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge(BaseEdge):
        """�������ıߵ���"""

        def __init__(self, u: "Graph.Vertex", v: "Graph.Vertex", x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoint(self) -> Tuple["Graph.Vertex", "Graph.Vertex"]:
            """�������˵��Ԫ��

            ��������ͼ������Ԫ��(u,v)������u�Ǳߵ���㣬����v���յ㣻
            ��������ͼ������Ԫ��(u,v)���䷽��������ġ�
            """
            return self._origin, self._destination

        def opposite(self, v: "Graph.Vertex") -> "Graph.Vertex":
            """���رߵ���һ������"""
            return self._destination if v is self._origin else self._origin

        def element(self):
            """���ؽڵ��ֵ"""
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        """����һ���յ�ͼ

        :param directed: �Ƿ�Ϊ����ͼ(True=����ͼ,False=����ͼ)
        """
        self._directed = directed
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    @property
    def is_directed(self) -> bool:
        """����ͼ�Ƿ�Ϊ����ͼ"""
        return self._incoming is not self._outgoing

    def vertex_count(self) -> int:
        """����ͼ�Ķ������Ŀ"""
        return len(self._outgoing)

    def vertices(self):
        """��������ͼ�����нڵ�"""
        return self._outgoing.keys()

    def edge_count(self) -> int:
        """����ͼ�ıߵ���Ŀ"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total // 2

    def edges(self):
        """��������ͼ�����б�"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u: "Graph.Vertex", v: "Graph.Vertex"):
        """��������򷵻شӶ���u������v�ıߣ����򷵻�None"""
        return self._outgoing[u].get(v)

    def degree(self, v: "Graph.Vertex", out: bool = True) -> int:
        """���ؽڵ�Ķ�/���/����

        ��������ͼ���������䵽����v�ıߵ���Ŀ��
        ��������ͼ���������䵽����v�������(out=True)������(out=False)�ıߵ���Ŀ
        """
        adj = self._outgoing if out else self._incoming
        return len(adj[v])

    def incident_edges(self, v: "Graph.Vertex", out: bool = True):
        """���������������䵽����v�ı�

        ��������ͼ���������䵽����v�ıߣ�
        ��������ͼ���������䵽����v�������(out=True)������(out=False)�ߵ���Ŀ
        """
        adj = self._outgoing if out else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None) -> "Graph.Vertex":
        """�����ͷ���һ���µĴ洢Ԫ��x�Ľڵ�(Vertex)"""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed:
            self._incoming[v] = {}
        return v

    def insert_edge(self, u: "Graph.Vertex", v: "Graph.Vertex", x=None) -> "Graph.Edge":
        """�����ͷ���һ���µĴӽڵ�u���ڵ�v�Ĵ洢Ԫ��x�ı�(Edge)"""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def remove_vertex(self, v: "Graph.Vertex"):
        """�Ƴ�����v��ͼ���������������"""
        del self._outgoing[v]
        if self.is_directed:
            del self._incoming[v]

    def remove_edge(self, e: "Graph.Edge"):
        """�Ƴ�ͼ�еı�e"""
        u, v = e.endpoint()
        del self._outgoing[u][v]
        del self._incoming[v][u]


def DFS(g: "Graph", u: "Graph.Vertex", discovered: Dict):
    """�����������"""
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


def construct_path(u: "Graph.Vertex", v: "Graph.Vertex", discovered: Dict):
    """������u��v������·��"""
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def DFS_complete(g: "Graph"):
    """����ͼ��ȫ��DFSɭ��"""
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)
    return forest


def BFS(g: "Graph", s: "Graph.Vertex", discovered: Dict):
    """�����������"""
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


def floyd_warshall(g: "Graph"):
    """Floyd_Warshall�㷨���㴫�ݱհ�"""
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])


def topological_sort(g: "Graph"):
    """����ͼ����������"""
    topo = []
    ready = []
    incount = {}
    for u in g.vertices():
        incount[u] = g.degree(u, out=False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo
