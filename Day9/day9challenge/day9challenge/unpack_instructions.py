from shutil import unpack_archive


def unpack_files(file, destination='unzipped'):
    # if not os.path.exists(destination):
    #     print('Creating directory')
    #     os.makedirs(destination)
    # else:
    #     print('Directory already exists')
    unpack_archive(file, destination)


