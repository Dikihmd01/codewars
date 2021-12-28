def perimeter(n):
    start = []
    n += 1
    for i in range(n):
        if i == 0:
            start.append(1)
        elif i == 1:
            start.append(1)
        else:
            start.append(sum(start[-2:]))
    return sum(start) * 4
