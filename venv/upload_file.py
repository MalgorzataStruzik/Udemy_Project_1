from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/FileUpload.html")
driver.maximize_window()

upload_input = driver.find_element_by_id("myFile")
path = os.path.abspath("upload.txt")
upload_input.send_keys(path)

driver.save_screenshot("screenshots/first.png")

driver.close()