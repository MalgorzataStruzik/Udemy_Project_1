from selenium import webdriver
from webdriver_manager.Chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/iFrameTest.html")
driver.maximize_window()

print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h1").text)