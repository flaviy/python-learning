text = "We are going to learn six methods in this chapter"
result = text
print(result)
result = text.upper()
print(result)
result = text.lower()
print(result)
result = text.split()  # ['We', 'are', 'going', 'to', 'learn', 'six', 'methods', 'in', 'this', 'chapter']
print(result)
result = text.split('o')  # ['We are g', 'ing t', ' learn six meth', 'ds in this chapter']
print(result)
a = "learning"
b = "methods"
c = "of"
d = "Python"
e = " "
result = e.join([a, b, c, d])  # learning methods of Python
print(result)
e = " - "
result = e.join([a, b, c, d])  # learning - methods - of - Python
print(result)
result = text.find('We')
print(result)
result = text.find('humans')
# -1, because it is not in the text,
# that is the difference between find and index, find returns -1
# if the substring is not found, index throws an exception
print(result)
result = text.count('e') # 5 because there are 5 'e' in the text
print(result)
result = text.replace('e', 'a')  # We ara going to laarn six mathods in this chaptar
print(result)
#replace several words at once
result = text.replace('e', 'a').replace('a', 'e')  # Wa ere geing te laern six methads in this cheptar
reversed_text = text[::-1]