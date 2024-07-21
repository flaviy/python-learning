import os
from pathlib import Path, PureWindowsPath, PurePath

print(os.getcwd())

#get current directory using Path
print(Path.cwd())

# add if not exists
'''
folder = Path("Day7")
if not os.path.exists(folder):
    os.mkdir(folder)'''

# write the same with pathlib
folder = Path(Path.cwd() / "Day7")
if not folder.exists():
    folder.mkdir()

folder2 = Path('test.txt')
print(folder2.read_text())
print(folder2.name)  # test.txt
print(folder2.suffix)  # .txt
print(folder2.stem)  # test

windows_path = PureWindowsPath(folder)
print(windows_path)

pure_path = PurePath(folder)
print(pure_path)
