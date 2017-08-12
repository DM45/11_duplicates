import os


def get_duplicate_files(directory):
    filename_list = []
    duplicate_file = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename in filename_list:
                duplicate_file.append(filename)
            else:
                filename_list.append(filename)
    return ' '.join(set(duplicate_file))


if __name__ == '__main__':
    _filepath = input('Enter directorys path for check: ')
    print('Duplicate files: ')
    print(get_filepaths(_filepath))
