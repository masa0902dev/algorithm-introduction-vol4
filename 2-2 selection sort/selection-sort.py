import random
import math
import sys; sys.path.append("."); import c;

# def selectionSort(list):
# 	a = copy.copy(list)

# 	for i in range(len(a)-1):
# 		min = a[i]
# 		iterator = i
# 		for j in range(i+1, len(a)):
# 			if min > a[j]:
# 				min = a[j]
# 				iterator = j
# 		a[iterator] = a[i]
# 		a[i] = min
# 	return a

def selectionSort(A):
	for i in range(len(A)-1):
		min_index = i
		for j in range(i+1, len(A)):
			if A[j] < A[min_index]:
				min_index = j
		A[i], A[min_index] = A[min_index], A[i]

A = [3,7,5,8,10,9,5,11]
A = random.choices(range(100), k=30)
selectionSort(A); c.c(A)