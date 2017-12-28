from datetime import *
def remonth(x):
    if x == 1:
        return 'January'
    if x == 2:
        return 'February'
    if x == 3:
        return 'March'
    if x == 4 :
        return 'April'
    if x == 5:
        return 'May'
    if x == 6:
        return 'June'
    if x == 7:
        return 'July'
    if x == 8:
        return 'August'
    if x == 9:
        return 'September'
    if x == 10:
        return 'October'
    if x == 11:
        return 'November'
    if x == 12:
        return 'December'
    
def month(x):
    if x == 'January':
        return 1
    if x == 'February':
        return 2
    if x == 'March' :
        return 3
    if x == 'April':
        return 4
    if x == 'May':
        return 5
    if x == 'June':
        return 6
    if x == 'July':
        return 7
    if x == 'August':
        return 8
    if x == 'September':
        return 9
    if x == 'October':
        return 10
    if x == 'November':
        return 11
    if x == 'December':
        return 12

for x in xrange(input()):
    a,b,c = raw_input().strip().split()
    mo = int(month(b))
    a,c = int(a),int(c)
    x = date(c,mo,a)
    u = x-timedelta(days = 1)
    r,t,y = u.year,u.month,u.day
    ty = (remonth(int(t)))
    print int(y),ty,int(r)