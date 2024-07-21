my_file = open('test.txt')
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# read and print the second line of the file
second_line = my_file.readline()
print(second_line)  # This is a test file.
print(my_file.readline().rstrip())  # This is a test file.
print(my_file.readline().rstrip())  # This is a test file.
print(my_file.readline().rstrip())  # This is a test file.
print(my_file.read().rstrip())  # This is a test file.
my_file.close()

print('*' * 50)

my_file = open('test.txt')


index = 0
for line in my_file:
    print('Here is says: ' + line.rstrip())
    index += 1
my_file.close()
print('*' * 50)
my_file = open('test.txt')
all = my_file.readlines()
# rstrip each line
all = [line.rstrip() for line in all]
print(all.pop())
print(all.pop())
print(all)
my_file.close()



record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]
file = open('register.txt', 'a')

file.writelines([line + '\t' for line in record_last_session])
file.close()
file = open('register.txt', 'r')
print(file.read())


