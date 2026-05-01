from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.maximize_window()
driver.get("https://www.selenium.dev")


wait = WebDriverWait(driver, 5)


btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_navbar"]/ul/li[2]/a')))


from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(btn1).perform()


btn1.click()
