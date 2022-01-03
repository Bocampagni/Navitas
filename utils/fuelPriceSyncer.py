from convertToNumber import convertToNumber
from getFuelList import getFuelList

fuel_list = getFuelList()
fuel_prices = convertToNumber(fuel_list)

print(fuel_prices)
