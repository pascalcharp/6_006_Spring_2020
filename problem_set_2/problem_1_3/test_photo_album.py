import unittest
from photo_album import PhotoAlbum


class TestPhotoAlbum(unittest.TestCase):
    def setUp(self):
        self.vide = PhotoAlbum()

    def test_construction_empty(self):
        self.assertFalse(self.vide)


if __name__ == '__main__':
    unittest.main()
