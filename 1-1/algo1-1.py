# f(n)が1秒で解ける最大の問題のサイズを求める。ただしアルゴリズムが問題を解くのにf(n)μsかかるとする。
import math


def lgn():
	p = 301029
	n = 1
	j = 0
	while math.log2(n) * 10**(-6) < 1:
		n += 10**p
		j += 1
		print(math.log2(n) * 10**(-6))
	return j, p

# lgn_get = lgn()
# print("max size: ", lgn_get[0], "* ( 10 **", lgn_get[1], ")")
# ANSWER: 10**301030


def root_n():
	n = 1
	while math.sqrt(n) * 10**(-6) < 1:
		n += 10**6
		print(math.sqrt(n) * 10**(-6))
	return n

# print(f'{root_n():e}')
# ANSWER: 10**12


def n_lgn():
	n = 1
	while n * math.log2(n) * 10**(-6) < 1:
		n += 1
		print(n * math.log2(n) * 10**(-6))
	return n

# print(n_lgn())
# ANSWER: 62746


def n_2jou():
	n = 1
	while n**2 * 10**(-6) < 1:
		n += 1
		print(n**2 * 10**(-6))
	return n

# print(n_2jou())
# ANSWER: 1000


def n_3jou():
	n = 1
	while n**3 * 10**(-6) < 1:
		n += 1
		print(n**3 * 10**(-6))
	return n

# print(n_3jou())
# ANSWER: 100


def two_njou():
	n = 1
	while 2**n * 10**(-6) < 1:
		n += 1
		print(2**n * 10**(-6))
	return n

# print(two_njou())
# ANSWER: 19


def n_factorial():
	n = 1
	while math.factorial(n) * 10**(-6) < 1:
		n += 1
		print(math.factorial(n) * 10**(-6))
	return n

print(n_factorial())
# ANSWER: 9