def initialize(arr,n):
	for i in xrange(n):
		arr[i] = i


def weighted_union(arr,size,a,b):
	root_a = root(a)
	root_b = root(b)
	if root_a == root_b:
		return
	if size[root_a] < size[root_b]:
		arr[root_a] = arr[root_b]
		size[root_b] += size[root_a]
	else:
		arr[root_b] = arr[root_a]
		size[root_a] += size[root_b]

def root(i):
	while arr[i] != i:
		arr[i] = arr[arr[i]]
		i = arr[i]
	return i

def find(a,b):
	if root(a) == root(b):
		return 1
	else:
		return 0
n,q = map(int,raw_input().split())
arr = [0]*n
initialize(arr,n)
size = [1]*n
for _ in xrange(q):
	ty = raw_input().split()
	if len(ty) == 3:
		weighted_union(arr,size,int(ty[1])-1,int(ty[2])-1)
	else:
		print size[root(int(ty[1])-1)]
		