import zipfile
import shutil
from pathlib import Path

my_zip = zipfile.ZipFile('my_zip.zip', 'w')

my_zip.write('file1.txt')
my_zip.write('file2.txt')
#create directory with pathlib

path = Path('extracted_files')
try:
    path.mkdir()
except FileExistsError:
    print('Directory already exists')

#
my_zip.close()
my_zip = zipfile.ZipFile('my_zip.zip', 'r')
try:
    my_zip.extractall(str(path))
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
my_zip.close()

source_folder = Path.home() / 'PycharmProjects' / 'pythonProject' / 'Day9' / 'extracted_files'
destination_file = Path.home() / 'PycharmProjects' / 'pythonProject' / 'Day9' / 'documents' / 'documents'

shutil.make_archive(str(destination_file), 'zip', source_folder)
print(str(destination_file)+'.zip')
shutil.unpack_archive(str(destination_file)+'.zip', source_folder / 'unzipped')
