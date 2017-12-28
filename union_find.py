def initialize(arr,n):
	for i in xrange(n):
		arr[i] = i
		

def weighted-union(arr,size,a,b):
	root_a = root(a)
	root_b = root(b)
	if size[root_a] < size[root_b]:
		arr[root_a] = arr[root_b]
		size[root_b] += size[root_a]
	else:
		arr[root_b] = arr[root_a]
		size[root_a] += size[root_b]

def root(arr,i):
	while arr[i] != i:
		arr[i] = arr[arr[i]]
		i = arr[i]
	return i

def find(a,b):
	if root(a) == root(b):
		return 1
	else:
		return 0

size = [1]*n