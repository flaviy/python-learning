from pathlib import Path


base = Path.home()
print(base) # /Users/username
guide = Path(base, 'Day6', Path('NewFolder','Subfolder', 'path1.py'))
print(guide) # /Users/username/Day6/NewFolder/Subfolder/path1.py


guide2 = guide.with_name('path2.py')
print(guide2) # /Users/username/Day6/NewFolder/Subfolder/path2.py

guide3 = guide.with_suffix('.txt')
print(guide3) # /Users/username/Day6/NewFolder/Subfolder/path1.txt

print(guide3.parent.parent) # /Users/username/Day6/NewFolder

all_files_path = Path(base / 'PyCharmProjects' / 'pythonProject')
print(all_files_path) # /Users/username/PyCharmProjects/pythonProject
#
#exclude .venv folder
for txt in Path(all_files_path).glob('**/*.py'):
    if '.venv' not in str(txt):
        print(txt)

guide_relative = guide.relative_to(Path(base, 'Day6'))
print(guide_relative) # NewFolder/Subfolder/path1.py


my_path = Path('C:/Users/User/Desktop/Python Course') / 'Quiz Day 6' / 'Question 1'
folder = my_path.parents[3]
print(folder) # C:\Users\User


