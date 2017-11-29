def median(l):
    sl = sorted(l)
    print sl
    llen = len(sl)
    if ((llen % 2) == 0):
        i = llen/2
        med = (sl[i] + sl[i-1])/2
    else:
        i = (llen-1)/2
        med = sl[i]
    return med

l = [4,5,4,5]
print median(l)