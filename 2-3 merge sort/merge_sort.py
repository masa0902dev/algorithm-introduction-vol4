import random
import math
import sys; sys.path.append("."); import c;

A = random.choices(range(100), k=30)
B = [1,2,3,1,1,2,9,6,7,6,6]

#   mergeSort(A, 0, n-1)が最初の呼び出し
def mergeSort(A, p = 0, r = len(A)-1):
    if p >= r:
        return
    q = math.floor((p+r)/2)
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    i = 0
    j = 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] >= R[j]:
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

mergeSort(A); c.c(A)
mergeSort(B); c.c(A)



# # mergeSort vs 要素数２になったらマージせずにソート->要素数３があり得るので要素数１ができちゃう->そうすると面倒になる->じゃあいいです。
# def mergeSortAlpha(A, p=0, r=len(A)-1):
#     if len(A) == 1:
#         return
#     if len(A) == 2 or len(A) == 3:
#         (A[p], A[r]) = (A[r], A[p]) if A[p] > A[r] else None
#         return
#     q = math.floor((p+r)/2)
#     mergeSortAlpha(A, p, q)
#     mergeSortAlpha(A, q+1, r)
#     merge(A, p, q, r)
# mergeSortAlpha(A); print(A)