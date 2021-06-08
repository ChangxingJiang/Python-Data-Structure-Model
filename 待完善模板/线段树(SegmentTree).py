# --*-- coding:GBK -- * --


"""�߶��� (Segment Tree) (Segment Tree)

����˼�루Lazy˼�룩�������������еĲ��������ڽ��������ǣ�����������ִ�У�ֱ�����ݲ�ѯ��������Ҫ�ֳ�������

������˵����

������˵����
self.N = �߶��������鳤��
self.H = �߶����ĸ߶�
self.update_fn = �����߶����ĺ���
self.query_fn = ��ѯ�߶����ĺ���
self.tree = [0] * (2 * N)  # �߶�������
self.lazy = [0] * N  # �߶���lazy����

������˵����
SegmentTree(N, update_fn, query_fn) ����һ�ó���ΪN���߶���
_apply(x, val)
_pull(x) ����Ҷ�ڵ�x�������Ƚڵ��ֵ������lazy���ԣ�
query(l, r) ��ѯ��l��r��ֵ

����˵����
SegmentTree = ������������ʵ�ֵ��߶���

"""


class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.update_fn = update_fn
        self.query_fn = query_fn

        # �����߶����ĸ߶�
        self.H = 1
        while (1 << self.H) < N:
            self.H += 1

        # ��ʼ���߶��������lazy�������飨lazy���Զ�Ӧ�����ڲ��ڵ㣩
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        """����x��ֵ������x���ӽڵ�ļ�����д��lazy������"""
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)  # ÿ���ڵ��lazy���Զ��Ǹ��ӽڵ��õ�

    def _pull(self, x):
        """����Ҷ�ڵ�x�������Ƚڵ��ֵ"""
        while x > 1:
            x >>= 1
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        """�Ӹ��ڵ����¼���x�����Ƚڵ��lazy�����е�ֵ"""
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, h):
        # ����L��R��Ӧ��Ҷ�ڵ�����
        l += self.N
        r += self.N

        # ��Ҷ�ڵ㿪ʼ���ϸ���ֵ
        L0, R0 = l, r
        while l <= r:
            print("��������:", l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                self._apply(l, h)
                l += 1
            if r & 1 == 0:
                self._apply(r, h)
                r -= 1
            print("��ǰ����:", self.tree, self.lazy)
            l >>= 1
            r >>= 1

        # ����Ҷ�ڵ�x�������Ƚڵ��ֵ
        self._pull(L0)
        self._pull(R0)

        print("�������", self.tree, self.lazy)

    def query(self, l, r):
        """��ѯ��L��R���������䣩��ֵ"""

        # ����L��R��Ӧ��Ҷ�ڵ�����
        l += self.N
        r += self.N

        # ����Ӹ��ڵ����¼���x�����Ƚڵ��lazy�����е�ֵ����lazy�����е�ֵ���㵽�ڵ��У�
        self._push(l)
        self._push(r)

        # ��ѯָ����Χ�ĺ�
        ans = 0
        while l <= r:
            print(l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                ans = self.query_fn(ans, self.tree[l])
                l += 1
            if r & 1 == 0:
                ans = self.query_fn(ans, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ans


if __name__ == "__main__":
    def sum_(a, b):
        return a + b


    st = SegmentTree(8, sum_, sum_)
    print(st.update(3, 5, 1))
    # print(st.query(2, 5))
    # print(st.query(3, 5))
