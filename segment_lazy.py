import math
def createtreee(low,up,pos):
	global seg
	global arr
	if up == low:
		seg[pos] = arr[low]
		return 
	mid = (up+low)/2
	cretre(low,mid,2*pos+1) #recursion in left part
	cretre(mid+1,up,2*pos+2) 
	seg[pos] = seg[2*pos+1] +seg[2*pos+2]
	return
def query(low,up,mn,mx,pos):
	global seg
	if mn>=low and mx<= up:   #total surpress
		return seg[pos]
	elif mn>up or mx<low:
		return 0
	mid = (mx+mn)/2
	return query(low,up,mn,mid,2*pos+1)+query(low,up,mid+1,mx,2*pos+2) #partial surpress
def update(ind,pos,arrlow,arrup,y):
	global seg
	if arrup== arrlow:
		seg[pos] = y
		return
	mid = (arrup+arrlow)/2
	if ind<= mid:
		update(ind,2*pos+1,arrlow,mid,y)
	else:
		update(ind,2*pos+2,mid+1,arrup,y)
	seg[pos] = seg[2*pos+1]+seg[2*pos+2]
	return
n = input()
arr = map(int,raw_input().split())
for x in xrange(n):
	arr[x] = arr[x]%2
u = int(math.ceil(math.log(n)/math.log(2)))
u = 2**(u+1)-1
seg = [0]*u
cretre(0,n-1,0)
#print seg
tst = input()
for x in xrange(tst):
	q,x,y = map(int,raw_input().split())
	if q == 2:
		w = query(x-1,y-1,0,n-1,0)
		print w
	elif q == 1:
		w = query(x-1,y-1,0,n-1,0)
		print (y-x+1)-w
	else:
		update(x-1,0,0,n-1,y%2)
		