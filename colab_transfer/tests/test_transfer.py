import unittest
from pathlib import Path

import colab_transfer


class TestTransferMethods(unittest.TestCase):

    def get_dummy_data_root(self):
        data_root_folder_name = 'dummy_data_for_unit_test/'

        return data_root_folder_name

    def create_dummy_data(self):
        input_data_folder_name = self.get_dummy_data_root() + 'input/'

        inner_input_data_folder_name = input_data_folder_name + 'inner_folder/'
        Path(inner_input_data_folder_name).mkdir(exist_ok=True, parents=True)

        deeper_input_data_folder_name = input_data_folder_name + 'second_inner_folder/deeper_folder/'
        Path(deeper_input_data_folder_name).mkdir(exist_ok=True, parents=True)

        Path(input_data_folder_name + 'dummy_file.txt').touch(exist_ok=True)

        Path(inner_input_data_folder_name + 'inner_dummy_file.txt').touch(exist_ok=True)

        Path(deeper_input_data_folder_name + 'deep_inner_dummy_file.txt').touch(exist_ok=True)

        return

    def test_copy_file(self):
        self.create_dummy_data()

        input_file_name = 'dummy_file.txt'

        input_folder = 'dummy_data_for_unit_test/input/'

        output_data_folder_name = self.get_dummy_data_root() + 'output/'

        colab_transfer.copy_file(
            file_name=input_file_name,
            source=input_folder,
            destination=output_data_folder_name,
        )

        path_to_output_file = output_data_folder_name + input_file_name

        self.assertTrue(Path(path_to_output_file).exists())

    def test_copy_folder_structure(self):
        self.create_dummy_data()

        input_folder = 'dummy_data_for_unit_test/input/'

        output_data_folder_name = self.get_dummy_data_root() + 'output/'

        colab_transfer.copy_folder_structure(
            source=input_folder,
            destination=output_data_folder_name,
        )

        for input_file_name in [
            'dummy_file.txt',
            'inner_folder/inner_dummy_file.txt',
            'second_inner_folder/deeper_folder/deep_inner_dummy_file.txt',
        ]:
            path_to_output_file = output_data_folder_name + input_file_name

            self.assertTrue(Path(path_to_output_file).exists())


if __name__ == '__main__':
    unittest.main()
