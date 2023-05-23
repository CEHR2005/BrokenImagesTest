import unittest
from unittest.mock import patch, MagicMock
from main import find_broken_images


class TestFindBrokenImages(unittest.TestCase):

    @patch('main.webdriver.Chrome')
    @patch('main.requests.get')
    def test_find_broken_images(self, mock_get, mock_chrome):
        # Mock the behavior of webdriver and requests.get
        mock_chrome.return_value.find_elements.return_value = [
            MagicMock(get_attribute=MagicMock(return_value='http://example.com/image1.png')),
            MagicMock(get_attribute=MagicMock(return_value='http://example.com/image2.png')),
        ]
        mock_get.return_value.status_code = 200

        # Call the function
        result = find_broken_images()

        # Assert that the function returned an empty list (since none of the images are broken)
        self.assertEqual(result, [])

    @patch('main.webdriver.Chrome')
    @patch('main.requests.get')
    def test_find_broken_images_with_broken_image(self, mock_get, mock_chrome):
        # Mock the behavior of webdriver and requests.get
        mock_chrome.return_value.find_elements.return_value = [
            MagicMock(get_attribute=MagicMock(return_value='http://example.com/image1.png')),
            MagicMock(get_attribute=MagicMock(return_value='http://example.com/image2.png')),
        ]
        mock_get.return_value.status_code = 404

        # Call the function
        result = find_broken_images()

        # Assert that the function returned a list with the broken image
        self.assertEqual(result, ['http://example.com/image1.png', 'http://example.com/image2.png'])


if __name__ == '__main__':
    unittest.main()
