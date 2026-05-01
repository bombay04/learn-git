from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://th.trovit.com/baan/")

logo = driver.find_element(By.XPATH, '/html/body/header/a[1]/img')
logo.click()
# # for i in range(3):
# #     logo = driver.find_element(By.XPATH, '/html/body/header/a[1]/img')
# #     logo.click()
# #     time.sleep(1)
favbtn = driver.find_element(By.XPATH, '/html/body/header/a[2]')
favbtn.click()
time.sleep(1)
driver.back()
time.sleep(1)
postbtn = driver.find_element(By.XPATH, '/html/body/header/div[3]/a[1]')
postbtn.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
loginbtn = driver.find_element(By.XPATH, '/html/body/header/div[3]/a[2]')
loginbtn.click()
time.sleep(2)
driver.back()
driver.switch_to.window(driver.window_handles[0])


footbtn1 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[1]/main/a/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn1)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn1.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn2 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[2]/main/a[1]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn2)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn2.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn3 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[2]/main/a[2]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn3)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn3.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.back()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn4 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[3]/main/a[1]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn4)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn4.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn5 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[3]/main/a[2]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn5)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn5.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn6 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[4]/main/a[1]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn6)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn6.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
footbtn7 = driver.find_element(By.XPATH, '//*[@id="icons"]/section[4]/main/a[2]/img')
driver.execute_script("arguments[0].scrollIntoView(true);", footbtn7)
time.sleep(1) # รอให้หายสั่นนิดนึง
footbtn7.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

time.sleep(5)


# keyword = "ที่ดินสำหรับขาย"
# inputkeyword = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/div/input')
# inputkeyword.send_keys("ที่ดินสำหรับขาย")
# searchbtn = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/button')
# searchbtn.click()
# driver.get("https://th.trovit.com") # สั่งโหลดหน้าหลักใหม่เลย
# time.sleep(2)





# search btn and click

# keyword = "ที่ดินสำหรับขาย"
# inputkeyword = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/div/input')
# inputkeyword.send_keys("ที่ดินสำหรับขาย")
# searchbtn = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/button')
# searchbtn.click()

# element = driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/article[1]/a/div[2]/div[2]/span/div/button')
# element.click()

# copy paste and click 
# tx = driver.find_element(By.XPATH, '/html/body/main/section[2]/div[1]/ul/li[3]/a')
# tx.send_keys(Keys.CONTROL+'c')
# inputkeyword = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/div/input')
# inputkeyword.send_keys(tx.text)
# searchbtn = driver.find_element(By.XPATH, '//*[@id="home-search-form-id"]/button')
# searchbtn.click()

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(10)

# driver.close()