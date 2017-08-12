import os


def get_duplicate_files(directory):
    file_info_list = []
    duplicate_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_info = (
                (filename, os.path.getsize((os.path.join(root, filename)))))
            if file_info in file_info_list:
                duplicate_list.append(file_info)
            else:
                file_info_list.append(file_info)
    return duplicate_list


if __name__ == '__main__':
    _filepath = input('Enter directorys path for check: ')
    print('Duplicate files: ')
    print(get_duplicate_files(_filepath))
