print("Enter your long text: ")
lines = []
while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break
long_text = ' '.join(lines)
print(long_text)


long_text = long_text.strip()

# enter 3 random letters, separated  by comma,  and save them to a list as 3 elements, e.g. ['a', 'b', 'c']. check that it is 1 letter, not more or digit

letterList = []

letterList.append(input("Enter 1 random letter: ").lower())
letterList.append(input("Enter 2 random letter: ").lower())
letterList.append(input("Enter 3 random letter: ").lower())
print(letterList)

# calculate the number of occurrences of each letter in the text
letterDict = {}
for letter in letterList:
    letterDict[letter] = long_text.count(letter)
print(letterDict)

# navigate through letterDict and print the letter and the number of occurrences
for letter, count in letterDict.items():
    print(f"Letter: {letter}, count: {count}")


# calculate the number of occurrences of each word in the text
wordDict = {}
words = long_text.split()
for word in words:
    # if word is not letter, skip it
    if not word.isalpha():
        continue
    wordDict[word] = words.count(word)


# navigate through wordDict and print the word and the number of occurrences
for word, count in wordDict.items():
    print(f"Word: {word}, count: {count}")

# total number of words in the text
print(f"Total number of words in the text: {len(words)}")

# the first letter of the text is
print(f"The first letter of the text is: {long_text[0]}")

index = -1
# the last letter of the text is
while not long_text[index].isalpha():
    index -= 1
    continue
print(f"The last letter of the text is: {long_text[index]}")

print(' '.join(words[::-1]))  # it will print the text in reverse order

print('Check if the word python is in the text')
print('python' in long_text)  # check if the word 'python' is in the text






