def f(i,x = []):
    print i,'i'
    print x,'x'
    u = x.append(i)
    print u,'u'
    x.append(u)
    return x
for x in range(3):
    y = f(x)
    print y,'ans'