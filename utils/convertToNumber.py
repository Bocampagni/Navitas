def convertToNumber(list):
    data = []
    for element in list:
        data.append(float((element[3:])))
    return data