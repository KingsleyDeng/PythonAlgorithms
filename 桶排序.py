# encoding: utf-8
"""
@author: kingsley
@contact: kingsleydeng1993@gmail.com
@time: 2020/5/29 19:34
@file: 桶排序.py
@desc: 
"""


def bucket_sort(lst):
    buckets = [0] * ((max(lst) - min(lst)) + 1)
    for i in range(len(lst)):
        buckets[lst[i] - min(lst)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(lst)] * buckets[i]
    return print(res)


if __name__ == '__main__':
    # main()
    list1 = [9, 10, 1, 4, 2, 7]
    bucket_sort(list1)
