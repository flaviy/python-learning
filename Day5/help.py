dic = {"key1": "value1", "key2": "value2", "key3": "value3"}
item = dic.popitem()
print(item)  # ('key3', 'value3')

str = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#" # remove all special characters at th left using lstrip
print(str.lstrip(",:_#"))  # Total_ _Pyt%on,,,,,,::#

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, "apple")
print(fruits)  # ['mango', 'banana', 'cherry', 'apple', 'plum', 'grapefruit']

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

print(phone_brands.isdisjoint(tv_brands))  # False
