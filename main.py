import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://the-internet.herokuapp.com/broken_images")
image_list = driver.find_elements(By.TAG_NAME, "img")
print('Total number of images on the page are ' + str(len(image_list)))

broken_images = []
for img in image_list:
    try:
        response = requests.get(img.get_attribute('src'), stream=True)
        if response.status_code != 200:
            broken_images.append(img.get_attribute('outerHTML'))
            print(img.get_attribute('outerHTML') + " is broken.")
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other Exception")

driver.quit()

print('The page has ' + str(len(broken_images)) + ' broken images')
