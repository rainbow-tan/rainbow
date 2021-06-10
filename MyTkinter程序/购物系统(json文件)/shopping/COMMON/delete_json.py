import os


def traverse_folder(folder, only_first=False):
    folder = os.path.abspath(folder)
    all_files = []
    all_dirs = []
    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder):
            for one_file in files:
                all_files.append(os.path.join(root, one_file))  # 所有文件
            for one_dir in dirs:
                all_dirs.append(os.path.join(root, one_dir))  # 所有文件夹
            if only_first:
                break
    else:
        msg = 'Can not find folder({}) for traverse'.format(folder)
        print(msg)
    return all_dirs, all_files


if __name__ == '__main__':
    for file in traverse_folder(os.path.abspath('../'))[1]:
        if file.endswith('.json'):
            os.remove(file)
            print('Remove file({})'.format(os.path.basename(file)))
