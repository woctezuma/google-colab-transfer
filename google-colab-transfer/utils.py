def get_path_to_root():
    path_to_root = '/content/'

    return path_to_root


def get_path_to_root_of_google_drive():
    path_to_root_of_google_drive = get_path_to_root() + 'drive/'

    return path_to_root_of_google_drive


def get_path_to_home_of_local_machine():
    path_to_home_of_local_machine = get_path_to_root()

    return path_to_home_of_local_machine


def get_path_to_home_of_google_drive():
    path_to_home_of_google_drive = get_path_to_root_of_google_drive() + 'My Drive/'

    return path_to_home_of_google_drive


def main():
    for folder in [
        get_path_to_root(),
        get_path_to_root_of_google_drive(),
        get_path_to_home_of_local_machine(),
        get_path_to_home_of_google_drive(),
    ]:
        print('Folder: {}'.format(folder))

    return True


if __name__ == '__main__':
    main()
