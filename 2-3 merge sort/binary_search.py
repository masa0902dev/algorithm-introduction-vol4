import random
import math
import sys; sys.path.append("."); import c;
A = random.choices(range(100), k=30)
# 配列をソート済みにする。
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



# 繰り返しVer。こっちの方が2分探索として書きやすい！！！O(lgn)。
def binarySearch(A, left, right, x):
	while left <= right: #left==rightでもまだ動作する
		mid = math.floor((left+right)/2)
		if A[mid] > x:
			right = mid - 1
		elif A[mid] < x:
			left = mid + 1
		else:
			return mid
	return None

target_value = 44
print(binarySearch(A, 0, len(A)-1, target_value))


# 2分探索: 最悪実行時間O(lgn)である。再帰的Ver。
def binarySearchByRecursion(A, p, r, target_value):
	if p >= r:
		print(target_value, "IS NOT FOUND")
		return
	q = math.floor((p+r)/2)
	if A[q] > target_value:
		r = q
		binarySearchByRecursion(A, p, r, target_value)
	elif A[q] < target_value:
		p = q+1
		binarySearchByRecursion(A, p, r, target_value)
	else:
		print("TARGET VALUE INDEX =", q, "(0 ~ n-1)")
		return

# binarySearchByRecursion(A, 0, len(A)-1, target_value)


