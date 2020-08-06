from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Test.html")
driver.maximize_window()

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")

checkbox.click()

if checkbox.is_selected():
    print("wartosc jest zaznaczona, odznaczamy")
    checkbox.click()
else:
    print("wartosc zaznaczamy")
    checkbox.click()