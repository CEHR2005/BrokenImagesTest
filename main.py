import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_broken_images():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://the-internet.herokuapp.com/broken_images")
    image_list = driver.find_elements(By.TAG_NAME, "img")

    broken_images = []
    for img in image_list:
        try:
            response = requests.get(img.get_attribute('src'), stream=True)
            if response.status_code != 200:
                broken_images.append(img.get_attribute('outerHTML'))
        except requests.exceptions.MissingSchema:
            pass
        except requests.exceptions.InvalidSchema:
            pass
        except:
            pass

    driver.quit()

    return broken_images
