def update(ind, val ):
    while (ind < 2*n+1):
        bit[ind] += val
        ind += ind & (-ind)


def su(ind):
    res = 0
    while (ind > 0):
        res += bit[ind]
        ind -= ind & (-ind)

    return res



n = input()
bit = [0]*(2*n+1)
a = [0]
a.extend(map(int, raw_input().split()))
a.extend(a[1:])
for x in xrange(n + 1, n + n+1):
    y = a[x]
    if y >= n:
        continue
    update(x - n + 1, 1)
    update(x - y + 1, -1)

sux = -1
ans = 0
for x in xrange(1, n + 1):
    temp = su(x)
    temp += su(x+n)
    if temp > sux:
        sux = temp
        ans = x
print(ans)
