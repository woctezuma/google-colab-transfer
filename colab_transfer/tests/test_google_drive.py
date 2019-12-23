import unittest

import colab_transfer


class TestGoogleDriveMethods(unittest.TestCase):
    def test_mount_google_drive(self):
        colab_transfer.mount_google_drive()
        self.assertTrue(True)

    def test_is_google_drive_mounted(self):
        google_drive_is_mounted = colab_transfer.is_google_drive_mounted()
        self.assertTrue(google_drive_is_mounted is not None)


if __name__ == '__main__':
    unittest.main()
