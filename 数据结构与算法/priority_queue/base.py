from abc import ABCMeta
from abc import abstractmethod


class BasePriorityQueue(metaclass=ABCMeta):
    """���ȼ����еĳ������"""

    class Item:
        """�������ļ�ֵ����"""
        __slots__ = ("_key", "_value")

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other: "BasePriorityQueue.Item"):
            return self._key < other._key

    @abstractmethod
    def add(self, k, v):
        """�����ȼ������в���һ��ӵ�м�k��ֵv��Ԫ��"""

    @abstractmethod
    def min(self):
        """����һ��Ԫ��(k,v)���������ȼ�����P��һ����������ֵ��Ԫ�飬��Ԫ��ļ�ֵ����Сֵ

        �������Ϊ�գ�����������
        """

    @abstractmethod
    def remove_min(self):
        """�����ȼ�����P���Ƴ�һ��ӵ����С��ֵ��Ԫ�飬���ҷ���������Ƴ���Ԫ��

        �������Ϊ�գ�����������
        """

    def is_empty(self):
        """������ȼ����в������κ�Ԫ�飬������True"""
        return len(self) == 0

    @abstractmethod
    def __len__(self):
        """�������ȼ�������Ԫ�ص�����"""
