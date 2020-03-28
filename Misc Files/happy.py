### HAPPY tree and "Melancoil"
### https://youtu.be/_DpzAvb3Vk4
### https://en.wikipedia.org/wiki/Happy_number

def happy_child(n):
	"""Return the next number in the happy sequence, 
	derived by summing the squares of the digits of N

	>>> happy_child(13)
	10
	>>> happy_child(145)
	42
	"""
	sum = 0
	while n > 0:
		sum, n = sum + (n % 10) ** 2, n // 10
	return sum


def new_happy_child(n):
	"""Return the next number in the happy sequence, 
	derived by summing the squares of the digits of N

	>>> new_happy_child(13)
	10
	>>> new_happy_child(145)
	42
	"""
	return process_digit(n, lambda mapped, place, d: mapped+d*d, lambda d: False, lambda mapped,place,d:None)

def happy_v1(n):
	"""Return True if the number is happy, otherwise False.
	A happy number is one which, after going through successive
	new_happy_children (summing the squares of the digits) becomes 1.
	While this is normally coded recursively, we're lucky that all numbers
	less than 1000 don't take more than 20 numbers until they converge, and
	if they don't, they're not in the happy tree (thus they're not happy)

	>>> happy_v1(7)
	True
	>>> happy_v1(6)
	False
	"""
	count = 0
	while count < 25 and n != 1:
		count, n = count + 1, happy_child(n)
	return n == 1

#print(happy_v1(6))

def happy_dot(n):
	"""Print a dot file based on the happy sequence staring at N
	https://www.graphviz.org/

	>>> happy_dot(7)
	digraph G {
	7->49
	49->97
	97->130
	130->10
	10->1
	}
	>>> happy_dot(4)
	digraph G {
	4->16
	16->37
	37->58
	58->89
	89->145
	145->42
	42->20
	20->4
	}
	"""
	count = 0
	seen = set()
	print("digraph G {")
	while count < 25 and n != 1:
		if n not in seen:
			print(str(n) + "->" + str(happy_child(n)))
			seen.add(n)
		count, n = count + 1, happy_child(n)
	print("}")

#happy_dot(4)
#happy_dot(7)

def happy_fancydot(orig_n,seen):
	"""Print the links of a graphviz dot file based on the happy sequence starting at N"""
	n = orig_n
	count = 0
	while count < 25 and n != 1:
		if n not in seen:
			print(str(n) + "->" + str(happy_child(n)))
			seen.add(n)
		count, n = count + 1, happy_child(n)
	if n == 1:
		print(str(orig_n) + " [ style = filled, color=yellow ];")
	elif orig_n in [89, 145, 42, 20, 4, 16, 37, 58]:
		print(str(orig_n) + " [ style = filled, color=red ];")
	else:
		print(str(orig_n) + " [ style = filled, color=green ];")

def happy_tree(n):
	"""Print a pretty dot file of the happy and 
	unhappy tree structure for numbers from 1 to N.
	Type:
	unix% python3 > happy.dot
	Then open that .dot file in GraphViz"""

	seen = set()
	print("digraph G {")
	while(n > 0):
		happy_fancydot(n, seen)
		n -= 1
	print("}")

happy_tree(100)