def comp(array1, array2):
    res = []
    if array1 is None or array2 is None: return False

    for i in range(len(array1)):
        res.append(array1[i]**2)
    return sorted(res) == sorted(array2)
