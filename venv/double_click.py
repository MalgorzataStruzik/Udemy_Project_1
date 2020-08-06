from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/DoubleClick.html")
driver.maximize_window()

button = driver.find_element_by_id("bottom")

webdriver.ActionChains(driver).double_click(button).perform