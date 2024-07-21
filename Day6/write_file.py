file = open('test2.txt', 'w')
file.write('This is a test file. \nSome another text.')
file.close()

file = open('test2.txt', 'a')
file.write('''
 This is a additionsal file. 
Some another text.
End of the file.
''')
file.writelines(['This is a test file. \n', 'Some another text.']) # pay attention to the newline character
file.close()