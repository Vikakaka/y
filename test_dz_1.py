import unittest
from app import get_doc_owner_name, delete_doc, add_new_doc


class TestControlPanelUnitTest(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("10006"), "Аристарх Павлов")

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('4005', 'passport', 'Irina', 3))

    def test_delete_doc(self):
        self.assertTrue(delete_doc(' '))


if __name__ == '__main__':
    unittest.main()