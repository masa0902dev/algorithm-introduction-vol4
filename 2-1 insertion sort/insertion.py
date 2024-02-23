import random
import math
import sys; sys.path.append("."); import c;
A = random.choices(range(100), k=30)


# 昇順
def insertionSort(A):
	for i in range(1, len(A)): # 1,2,...,n-1をループ。(2個目,3個目,...n個目)
		key = A[i]
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key
insertionSort(A)
c.c(A)

# 降順
B = random.choices(range(100), k=30)
def insertionSortDesc(B):
	for i in range(1, len(B)):
		key = B[i]
		j = i - 1
		while j >= 0 and B[j] < key:
		# やってることは元の部分配列コピーなので、たったlist[j] < keyの変更だけで降順になる
			B[j+1] = B[j]
			j -= 1
		B[j+1] = key
insertionSortDesc(B)
c.c(B,True)


# Searching Problem
C = random.choices(range(100), k=30)
def searchIndex(C, target_value):
	for i in range(0, len(C)):
		if C[i] == target_value:
			return i
	return None
print()
print(C)
print(searchIndex(C, 10))

insertionSort(C)
def searchSortedIndex(C, target_value):
	for i in range(0, len(C)):
		if C[i] == target_value:
			return i
	return None
print(C)
print(searchSortedIndex(C, 10))