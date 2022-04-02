def getNumberConversion(listTarget):
    data = []
    for element in listTarget:
        data.append(float((element[3:])))
    return data
