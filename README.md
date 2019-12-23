# Google Colab Transfer: transfer data between Colab & Drive

[![PyPI status][pypi-image]][pypi]
[![Build status][build-image]][build]
[![Publish status][publish-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]
  
This repository contains Python code to transfer data between [Google Colab](https://colab.research.google.com) and [Google Drive](https://www.google.com/drive/).

## Installation

The code is packaged for [PyPI](https://pypi.org/project/Google-Colab-Transfer/), so that the installation consists in running:

```bash
pip install colab_transfer
```

## Usage

### Get the path to the home folder of the local machine for your session on Google Colaboratory

```python
import colab_transfer

colab_path = colab_transfer.get_path_to_home_of_local_machine()
```

### Get the path to the home folder on Google Drive

```python
import colab_transfer

drive_path = colab_transfer.get_path_to_home_of_google_drive()
```

### Mount Google Drive

NB: you will have to manually input the authorization code.

```python
import colab_transfer

colab_transfer.mount_google_drive()
```

### Check whether Google Drive is mounted

```python
import colab_transfer

google_drive_is_mounted = colab_transfer.is_google_drive_mounted()
```

### Copy a file from Drive to Colaboratory 

```python
import colab_transfer

colab_path = colab_transfer.get_path_to_home_of_local_machine()
drive_path = colab_transfer.get_path_to_home_of_google_drive()

input_file_name = 'dummy_file.txt'

colab_transfer.copy_file(
    file_name=input_file_name,
    source=drive_path,
    destination=colab_path,
)
```

### Copy a file from Colaboratory to Drive 

```python
import colab_transfer

colab_path = colab_transfer.get_path_to_home_of_local_machine()
drive_path = colab_transfer.get_path_to_home_of_google_drive()

input_file_name = 'dummy_file.txt'

colab_transfer.copy_file(
    file_name=input_file_name,
    source=colab_path,
    destination=drive_path,
)
```

### Copy a folder structure from Drive to Colaboratory 

```python
import colab_transfer

colab_path = colab_transfer.get_path_to_home_of_local_machine()
drive_path = colab_transfer.get_path_to_home_of_google_drive()

input_folder_name = 'dummy_folder/'

colab_transfer.copy_folder_structure(
    source=drive_path + input_folder_name,
    destination=colab_path + input_folder_name,
)
```

### Copy a folder structure from Colaboratory to Drive 

```python
import colab_transfer

colab_path = colab_transfer.get_path_to_home_of_local_machine()
drive_path = colab_transfer.get_path_to_home_of_google_drive()

input_folder_name = 'dummy_folder/'

colab_transfer.copy_folder_structure(
    source=colab_path + input_folder_name,
    destination=drive_path + input_folder_name,
)
```

<!-- Definitions -->

  [pypi]: https://pypi.python.org/pypi/Google-Colab-Transfer
  [pypi-image]: https://badge.fury.io/py/Google-Colab-Transfer.svg

  [build]: <https://github.com/woctezuma/google-colab-transfer/actions>
  [build-image]: <https://github.com/woctezuma/google-colab-transfer/workflows/Python package/badge.svg?branch=master>
  [publish-image]: <https://github.com/woctezuma/google-colab-transfer/workflows/Upload Python Package/badge.svg?branch=master>

  [pyup]: https://pyup.io/repos/github/woctezuma/google-colab-transfer/
  [dependency-image]: https://pyup.io/repos/github/woctezuma/google-colab-transfer/shield.svg
  [python3-image]: https://pyup.io/repos/github/woctezuma/google-colab-transfer/python-3-shield.svg

  [codecov]: https://codecov.io/gh/woctezuma/google-colab-transfer
  [codecov-image]: https://codecov.io/gh/woctezuma/google-colab-transfer/branch/master/graph/badge.svg

  [codacy]: https://www.codacy.com/app/woctezuma/google-colab-transfer
  [codacy-image]: https://api.codacy.com/project/badge/Grade/8d61b0dec7c346289a73f4cc3a760c53
