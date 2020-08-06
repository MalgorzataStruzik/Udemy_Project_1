from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Desktop/Test.html")
#okno przelądarki otworzy się w max szerokosci
driver.maximize_window()
driver.find_element_by_id("clickOnMe")
driver.find_element_by_name("fname")
driver.find_element_by_link_text("Visit W3Schools.com!")
driver.find_element_by_class_name("topSecret")
driver.find_element_by_tag_name("a")

#selektory css
driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("p.topSecret")
#wyswietli nam tekst, ktory znajduje sie w konkretnym miejscu tablei
print(driver.find_element_by_css_selector("th:first-child").text)

# lokalizowanie za pomoca XPATH
driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
driver.find_element_by_xpath("//tbody//th")
driver.find_element_by_xpath("//th[text()='Month']")
driver.find_element_by_xpath("//th")
driver.find_element_by_xpath("//button[@id='clickOnMe']")

elements_list_length = len(driver.find_elements_by_xpath("//th"))
print(elements_list_length)


# wszystkie okna zamykają się
#driver.quit()
# zostaje zamknieta tylko bierzaca wybrana strona
driver.close()


