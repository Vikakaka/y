import unittest
from dz_test import create_folder


class TestCreateFolder(unittest.TestCase):
    def test_folder(self):
        self.assertEqual(create_folder('test'), 201)


if __name__ == '__main__':
    unittest.main()