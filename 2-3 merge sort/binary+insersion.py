import random
import math
import sys

sys.path.append(".")
import c

A = random.choices(range(100), k=30)


# 挿入ソートのソート済み部分配列A[1:j-1]の逆向き走査に線形探索を用いていたが、それを
# 2分探索にすると挿入ソートの最悪実行時間をO(n*lgn)にできるか？
# --> 結局、挿入操作はO(n)かかるから2分探索使ってもO(n^2)である！(確かに線形探索のinsertionよりは早くなるが。)
def insertionSort_byBinarySearch(A):
    for i in range(1, len(A)): #ここがlen(A)-1ではない<--普通のinsertion自体がそう！
        key = A[i]
        index = binarySearch(A, 0, i-1, key)
        A[index+1:i+1] = A[index:i]
        A[index] = key


def binarySearch(A, left, right, x):
    while left <= right:
        mid = math.floor((left+right)/2)
        if A[mid] > x:
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
        else:
            return mid
    return left #ここが普通の2分探索からの変更点

insertionSort_byBinarySearch(A)
c.c(A)