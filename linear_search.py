# _*_ coding=utf-8 _*_


def linear_search(data, val):
    """
    顺序查找：也称为线性查找，从列表第一个元素开始，按顺序进行搜索，直到找到元素或搜索到列表
    最后一个元素为止。
    时间复杂度：O(n)
    :param data:
    :param val:
    :return:
    """
    for i in range(len(data)):
        if data[i] == val:
            return i
        else:
            return
