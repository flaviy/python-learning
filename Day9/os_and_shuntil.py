import os
import shutil
from pathlib import Path
import send2trash

file = open('os_and_shuntil.text', 'w')
file.write('This is a test file.')
file.close()

print(os.listdir())

base = Path.home()
#move to the home directory
shutil.move('os_and_shuntil.text', base / 'Documents' / 'os_and_shuntil.text')
send2trash.send2trash(base / 'Documents' / 'os_and_shuntil.text')

print(os.walk(base)) # <generator object walk at 0x10f3b3f90>
for dirpath, subdirectory, filenames in os.walk(base / 'Documents'):
    print(f'In folder {dirpath}')
    print(f'Subfolders are: ')
    for sub in subdirectory:
        print(f'\t{sub}')
    print(f'Files are: ')
    for file in filenames:
        print(f'\t{file}')

