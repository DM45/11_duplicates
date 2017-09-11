import os


def get_duplicate_files(directorys_filepath):
    file_info_list = []
    duplicate_list = []
    for root, directories, all_files in os.walk(directorys_filepath):
        for filename in all_files:
            file_info = (
                (filename, os.path.getsize((os.path.join(root, filename)))))
            if file_info in file_info_list:
                duplicate_list.append(file_info)
            else:
                file_info_list.append(file_info)
    return [duplicate_file[0] for file in duplicate_list]


if __name__ == '__main__':
    directorys_filepath = input('Enter directory path for check: ')
    print('Duplicate files: ')
    if not os.path.exists(filepath):
        print('Wrong filepath!')
    else:
    	print(get_duplicate_files(directorys_filepath))
