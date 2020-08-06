from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Waits.html")
driver.maximize_window()

driver.find_element_by_id("clickOnMe").click()
print(driver.find_element_by_tag_name("p").text)