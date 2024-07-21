import re

text = 'if you need me help call me at 892-345-6789'


pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

result = pattern.search(text)

for finding in re.finditer(pattern, text):
    print(finding.span())  # (31, 43)
    print(finding.group())  # 892-345-6789

print(result.group())  # 892-345-6789

pattern = 'me'
result = re.findall(pattern, text)

print(result)  # ['me', 'me', 'me']

password = input('Enter your password: ')
pattern = re.compile(r'\d{1}\w{7}')
result = pattern.search(password)
#pattern.fullmatch()

if result:
    print('Password is valid')
else:
    print('Password is invalid')

text = 'sunday or monday the store is closed'


search = re.findall(r'sunday|monday', text)
for word in search:
    print(word)  # sunday monday

search = re.search(r'.lose', text)
print(search)

search = re.findall(r'[^\s]+', text) # ['sunday', 'or', 'monday', 'the', 'store', 'is', 'closed']
print(search)
print('-'.join(search)) # sunday-or-monday-the-store-is-closed






