from collections import Counter
s = raw_input()
n = len(s)
#print n
t = raw_input()
arr = Counter(s)
art = Counter(t)
qs = arr['?']
low = 0
high = n
#cnt = {}\\]
while True:
	if high < low:
		y = low-1	
		break
	y = (low+high)/2
	su = 0
	for u in art.keys():
		#cnt = {}
		if u != '?':
			su += art[u]*y - min(art[u]*y,arr.get(u,0))
			
	#print su,y,'y'
	if su < qs:
		low = y + 1
	elif su > qs:
		high = y - 1
	else:
		break
cnt = {}
for u in art.keys():
	if u!= '?':
		cnt[u] = art[u]*y - min(art[u]*y,arr.get(u,0))
s = list(s)
#print cnt
te = [ ]
for x,y in cnt.items():
	te.extend([x]*y)
for x in xrange(n):
	if s[x] == '?':
		if len(te) > 0:
			s[x] =te.pop()
		else:
			s[x] = 'a'
s = ''.join(s)
print s