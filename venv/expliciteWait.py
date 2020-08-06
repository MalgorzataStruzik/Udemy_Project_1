from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Waits2.html")
driver.maximize_window()

driver.find_element_by_id("clickOnMe").click()
wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 1 )
print(driver.find_element_by_tag_name("p").text)