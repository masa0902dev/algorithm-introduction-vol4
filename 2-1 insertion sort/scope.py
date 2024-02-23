def about_function():
	x2 = 10

	def sum(x1):
		x2 = 10000
		return x1 + x2

	print(sum(1))
	print(x2) # x2=10000はローカルな変更として、ここではx2=10が出力.
# about_function()


def about_while_for():
	import random
	A = list(random.sample(range(100), 10))
	print(A)
	for i in range(1, len(A)):
		key = A[i]
		j = i - 1
		print(i, ":", j, "->", end=" ")
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key
		print(j) # jはwhileループを抜けた後の値が出力される.これはローカルな変更ではなくグローバルのようだ。
	print(A)
	print(i) # forループを抜けた後の値が出力される.これはローカルな変更ではなくグローバルのようだ。
about_while_for()

#### Python, JSでは、ループを出た後も値を持ち続ける！
#### つまり、while, forでの値の変更はそのブロック内でグローバルに扱われる。
#### ちなみに、forではiは最後の繰り返しの値を保持。他の言語だと限界を最初に超える値を保持するらしい。