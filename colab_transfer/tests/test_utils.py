import unittest

import colab_transfer


class TestUtilsMethods(unittest.TestCase):

    def test_get_path_to_home_of_google_drive(self):
        path = colab_transfer.get_path_to_home_of_google_drive()
        self.assertEqual(path, '/content/drive/My Drive/')

    def test_get_path_to_home_of_local_machine(self):
        path = colab_transfer.get_path_to_home_of_local_machine()
        self.assertEqual(path, '/content/')


if __name__ == '__main__':
    unittest.main()
