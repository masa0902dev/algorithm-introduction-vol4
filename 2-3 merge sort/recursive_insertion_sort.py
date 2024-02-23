import random
import math
import sys; sys.path.append("."); import c;

def recursiveInsertionSort(A, r):
    if r <= 0:
        return
    recursiveInsertionSort(A, r-1)
    key = A[r]
    j = r - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
    
A = [1,5,4,6,1,7,7,4,10,1]
A = random.choices(range(100), k=30)
recursiveInsertionSort(A, len(A)-1)
c.c(A)