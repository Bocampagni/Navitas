
def getShippingPrice(distance):
    return {
        "car": {
            "gasoline": distance * 7,
            "ethanol": distance * 5.9,
            "gnv": distance * 5,
            "diesel": distance * 4
        },
        "motorcycle": {
            "gasoline": distance * 6
        }
    }
