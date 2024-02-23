import random
import math
import sys; sys.path.append("."); import c;
A = random.choices(range(100), k=30)


#   mergeSort(A, 0, n-1)が最初の呼び出し
def mergeSort(A, left=0, right=len(A)-1):
    if left >= right:
        return
    mid = math.floor((left+right)/2)
    mergeSort(A, left, mid)
    mergeSort(A, mid+1, right)
    merge(A, left, mid, right)

def merge(A, left, mid, right):
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

mergeSort(A); c.c(A)



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