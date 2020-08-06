from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Desktop/Test.html")
driver.maximize_window()

#klikanie na element i obsługa alertu
driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.accept()

# drugi sposob obslugi alertu
driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.dismiss()

#wprowadzenie wartosci do agu input
driver.find_element_by_id("fname").send_keys("Bartek")
#sylmulacja przycisku ENTER
#driver.find_element_by_name("password").send_keys(Keys.ENTER)
# wybieranie opcji z select
auto_select = Select(driver.find_element_by_tag_name("select"))
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(0)

#zaznaczanie checkbox'a
driver.find_element_by_xpath("//input[@type='checkbox']").click()

# wybór opcji w radiobutton
driver.find_element_by_xpath("//input[@value='male']").click()

#pobieranie teksu z web elementu
print(driver.find_element_by_xpath("//input[@value='male']").text)
print(driver.find_element_by_tag_name("h1").text)
print(driver.find_element_by_id("clickOnMe").text)

#pobieranie teksu ukrytego
print(driver.find_element_by_tag_name("p").get_attribute("textContent"))

# czy obrazek się wyświetla
print(driver.find_element_by_id("smileImage").size.get("height"))

#przełączanie do nowo otwartego okna przeglądarki

driver.quit()