import math

value = round(5.35345435345345)  # it will round the number to the closest integer based on math rules

print(type(value))  # it will return an integer

value = round(5.35345435345345, 3)
print(value)  # it will return 5.353, float

valueName = 5.6587978787

print(math.floor(valueName))  # floor valueName to the closest integer down, so result should be 5
print(math.ceil(valueName))  # ceil valueName to the closest integer up, so result should be 6

print(round(13 / 2, 0))  # 6.0, float
print(round(13 / 2))  # 6, integer



