from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Test.html")
driver.maximize_window()

first_name_input = driver.find_element_by_id("fname")

if first_name_input.is_enabled():
    first_name_input.click()
else:
    print("nie jest dostępny")