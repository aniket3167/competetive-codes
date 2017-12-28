n = input()
a = map(int, raw_input().split())
b, su, val, ans = [], 0, dict(), 1
for x in xrange(n):
    b.append(a[x] - x)
    if b[x] <= 0:
        su += 1
    val[b[x]] = val.get(b[x], 0) + 1
mx = su
for x in xrange(n - 1):
    val[b[x]] -= 1
    if b[x] <= 0:
        su -= 1
    b[x] = a[x] - n + 1
    if b[x] <= 0:
        su += 1
    val[b[x]] = val.get(b[x], 0) + 1
    su = su - val.get(-x, 0)
    if su > mx:
        mx = su
        ans = x + 2
print ans
