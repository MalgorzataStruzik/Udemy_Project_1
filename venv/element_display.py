from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Test.html")
driver.maximize_window()

paragraf = driver.find_element_by_tag_name("p")
if paragraf.is_displayed():
    print("Is displayed")
    print(paragraf.text)
else:
    print("is not dispalyed")
    print(paragraf.get_attribute("textContent"))