import os


def read_all_files_from_subfolders(folder):
    #  Get all files from all subfolders and return file content using a generator
    for root, dirs, files in os.walk(folder):
        # print('*' * 50)
        # print(f'Root: {root}')
        # print(f'Directories: {dirs}')
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                yield file, f.read()
