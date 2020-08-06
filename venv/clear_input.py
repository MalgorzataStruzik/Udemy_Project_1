from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Desktop/Test.html")
driver.maximize_window()

username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("ponuryAdam")