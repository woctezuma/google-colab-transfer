from pathlib import Path

from colab_transfer.utils import get_path_to_root_of_google_drive

try:
    from google.colab import drive
except ModuleNotFoundError:
    pass


def mount_google_drive():
    try:
        drive.mount(get_path_to_root_of_google_drive())
    except NameError:
        print('Google Drive cannot be mounted. Please ensure that a session of Colaboratory is running.')

    return


def is_google_drive_mounted():
    google_drive_is_mounted = Path(get_path_to_root_of_google_drive()).exists()

    return google_drive_is_mounted


def main():
    mount_google_drive()

    print('Is Google Drive mounted? {}'.format(is_google_drive_mounted()))

    return True


if __name__ == '__main__':
    main()
