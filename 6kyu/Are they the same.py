def comp(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i]**2)
    res.sort()
    b.sort()
    return True if res == b else 0
