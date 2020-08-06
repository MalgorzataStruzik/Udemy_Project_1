from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Desktop/Test.html")
driver.maximize_window()
driver.execute_script("arguments[0].click();",driver.find_element_by_id("newPage"))

wartosc = "bartek"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')",driver.find_element_by_id("fname"))
