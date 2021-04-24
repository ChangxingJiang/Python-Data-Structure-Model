# -*-coding:GBK -*-

"""
�������

BaseVertex �������ıߵĳ������
BaseGraph ͼ�ĳ������
"""

from abc import ABCMeta
from abc import abstractmethod


class BaseVertex(metaclass=ABCMeta):
    """�������Ľڵ�ĳ������"""
    __slots__ = ("_element",)

    @abstractmethod
    def element(self):
        """���ؽڵ��ֵ"""


class BaseEdge(metaclass=ABCMeta):
    """�������ıߵĳ������"""
    __slots__ = ("_origin", "_destination", "_element")

    @abstractmethod
    def endpoint(self):
        """�������˵��Ԫ��

        ��������ͼ������Ԫ��(u,v)������u�Ǳߵ���㣬����v���յ㣻
        ��������ͼ������Ԫ��(u,v)���䷽��������ġ�
        """

    @abstractmethod
    def opposite(self, v):
        """���رߵ���һ������"""

    @abstractmethod
    def element(self):
        """���ؽڵ��ֵ"""


class BaseGraph(metaclass=ABCMeta):
    """ͼ�ĳ������"""

    @abstractmethod
    def vertex_count(self):
        """����ͼ�Ķ������Ŀ"""

    @abstractmethod
    def vertices(self):
        """��������ͼ�����нڵ�"""

    @abstractmethod
    def edge_count(self):
        """����ͼ�ıߵ���Ŀ"""

    @abstractmethod
    def edges(self):
        """��������ͼ�����б�"""

    @abstractmethod
    def get_edge(self, u, v):
        """��������򷵻شӶ���u������v�ıߣ����򷵻�None"""

    @abstractmethod
    def degree(self, v, out=True):
        """���ؽڵ�Ķ�/���/����

        ��������ͼ���������䵽����v�ıߵ���Ŀ��
        ��������ͼ���������䵽����v�������(out=True)������(out=False)�ıߵ���Ŀ
        """

    @abstractmethod
    def incident_edges(self, v, out=True):
        """���������������䵽����v�ı�

        ��������ͼ���������䵽����v�ıߣ�
        ��������ͼ���������䵽����v�������(out=True)������(out=False)�ߵ���Ŀ
        """

    @abstractmethod
    def insert_vertex(self, x=None):
        """�����ͷ���һ���µĴ洢Ԫ��x�Ľڵ�(Vertex)"""

    @abstractmethod
    def insert_edge(self, u, v, x=None):
        """�����ͷ���һ���µĴӽڵ�u���ڵ�v�Ĵ洢Ԫ��x�ı�(Edge)"""

    @abstractmethod
    def remove_vertex(self, v):
        """�Ƴ�����v��ͼ���������������"""

    @abstractmethod
    def remove_edge(self, e):
        """�Ƴ�ͼ�еı�e"""
