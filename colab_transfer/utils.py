def get_path_to_root():
    return '/content/'


def get_path_to_root_of_google_drive():
    return get_path_to_root() + 'drive/'


def get_path_to_home_of_local_machine():
    return get_path_to_root()


def get_path_to_home_of_google_drive():
    return get_path_to_root_of_google_drive() + 'My Drive/'


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
