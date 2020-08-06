from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/BMww/Desktop/Test.html")
driver.maximize_window()
driver.find_element_by_id("newPage").click()
print(driver.title)
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print(driver.title)
driver.switch_to.window(current_window_name)
print(driver.title)

driver.quit()