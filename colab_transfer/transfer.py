import glob
import os
import shutil
from pathlib import Path

from colab_transfer.google_drive import is_google_drive_mounted, mount_google_drive
from colab_transfer.utils import (
    get_path_to_home_of_google_drive,
    get_path_to_home_of_local_machine,
)


def copy_file(file_name, source=None, destination=None, verbose=True):
    if not is_google_drive_mounted():
        mount_google_drive()

    if source is None:
        source = get_path_to_home_of_google_drive()

    if destination is None:
        destination = get_path_to_home_of_local_machine()
    else:
        Path(destination).mkdir(parents=True, exist_ok=True)

    input_file_name = source + file_name
    output_file_name = destination + file_name

    if Path(output_file_name).exists():
        if verbose:
            print(f'File {output_file_name} already exists. Copy skipped.')
    else:
        if verbose:
            print(f'Copying {input_file_name} to {output_file_name}')

        try:
            shutil.copyfile(input_file_name, output_file_name)
        except FileNotFoundError:
            print(f'File {input_file_name} could not be found. Copy aborted.')

    return


def copy_folder(folder_name, source=None, destination=None, verbose=True):
    if not is_google_drive_mounted():
        mount_google_drive()

    if source is None:
        source = get_path_to_home_of_google_drive()

    if destination is None:
        destination = get_path_to_home_of_local_machine()
    else:
        Path(destination).mkdir(parents=True, exist_ok=True)

    input_folder_name = source + folder_name
    output_folder_name = destination + folder_name

    if Path(output_folder_name).exists():
        if verbose:
            print(f'Folder {output_folder_name} already exists. Copy skipped.')
    else:
        if verbose:
            print(f'Copying {input_folder_name} to {output_folder_name}')

        try:
            shutil.copytree(src=input_folder_name, dst=output_folder_name)
        except FileNotFoundError:
            print(
                f'Folder {input_folder_name} could not be found. Copy aborted.',
            )

    return


def copy_folder_structure(source=None, destination=None, verbose=True):
    if not is_google_drive_mounted():
        mount_google_drive()

    if source is None:
        source = get_path_to_home_of_google_drive()

    if destination is None:
        destination = get_path_to_home_of_local_machine()
    else:
        Path(destination).mkdir(parents=True, exist_ok=True)

    files_and_folders = glob.glob(source + '*')

    root_files = glob.glob(source + '*.*')
    root_folders = set(files_and_folders).difference(root_files)

    if verbose:
        print(f'Files: {root_files}')
        print(f'Folders: {root_folders}')

    for f_name in root_files:
        file_name = os.path.basename(f_name)

        copy_file(file_name, source=source, destination=destination, verbose=verbose)

    for f_name in root_folders:
        folder_name = os.path.basename(f_name) + '/'

        copy_folder(
            folder_name,
            source=source,
            destination=destination,
            verbose=verbose,
        )

    return


def main():
    return True


if __name__ == '__main__':
    main()
