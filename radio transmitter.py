def transmitter(boolen, ranger, total):
    marker = ranger
    total_count = 0
    flag = 0
    for x in xrange(total):
        if marker > ranger:
            marker -= 1
            continue
        if boolen[x] == 1:
            flag = 1
            last = x
        if flag == 1:
            marker -= 1
            if marker < 0:
                total_count += 1
                marker = ranger + ranger - x + last
                flag = 0
    if flag == 1 and marker <= ranger:
        total_count += 1
    return total_count


h, ranger = map(int, raw_input().split())
gh = 0
array = map(int, raw_input().split())
array.sort()
total = array[-1] + 1
boolen = [0] * total
boolen2 = [0] * total
y = 12
for x in array:
    boolen[x] = 1
    boolen2[total - x - 1] = 1
ci = transmitter(boolen, ranger, total)
si = transmitter(boolen2, ranger, total)
print min(si, ci)

