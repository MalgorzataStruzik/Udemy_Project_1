from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Documents/Nowy%20folder/Test.html")
driver.maximize_window()

elements = driver.find_elements_by_tag_name("papa")
if len(elements )> 0:
     print("element istnieje na stronie")
else:
    print("nie istnieje")
try:
    driver.find_element_by_tag_name("papap")
    print("element istnieje na sstonie")
except NoSuchElementException:
    print(" elemenet nie istnieje")