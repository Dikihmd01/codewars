def rgb(r, g, b):
    list = [r, g, b]
    decToHex = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    rgbList = []
    res = []
    for k in range(len(list)):
        if list[k] < 0: list[k] = 0
        if  list[k] > 255: list[k] = 255
        rgbList.append(list[k])
    

    res.append(decToHex[int(rgbList[0]/16)])
    res.append(decToHex[(rgbList[0]/16 - int(rgbList[0]/16)) * 16])
    res.append(decToHex[int(rgbList[1]/16)])
    res.append(decToHex[(rgbList[1]/16 - int(rgbList[1]/16)) * 16])
    res.append(decToHex[int(rgbList[2]/16)])
    res.append(decToHex[(rgbList[2]/16 - int(rgbList[2]/16)) * 16])

    return "".join([str(list) for list in res])
