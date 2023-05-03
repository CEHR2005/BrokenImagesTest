import requests
from selenium import webdriver
import unittest


class BrokenImagesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="path/to/chromedriver")

    def test_broken_images(self):
        self.driver.get("https://example.com")
        images = self.driver.find_elements_by_tag_name("img")

        for image in images:
            src = image.get_attribute("src")
            try:
                response = requests.get(src)
                if response.status_code != 200:
                    print("Broken image:", src)
            except Exception as e:
                print("Error checking image:", src)
                print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
