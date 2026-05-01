from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://store.steampowered.com/?l=thai")
buttom = driver.find_element(By.XPATH, '//*[@id="tab_trendingfree_content_trigger"]/div')
buttom.click()
gamename = driver.find_elements(By.XPATH, '//*[@id="tab_trendingfree_content"]/div/a/div[4]/div[1]')
price = driver.find_elements(By.XPATH, '//*[@id="tab_trendingfree_content"]/div/a/div[3]/div/div')
ty = driver.find_elements(By.XPATH, '//*[@id="tab_trendingfree_content"]/div/a/div[4]/div[2]/div')
time.sleep(5)
for game, price, ty in zip(gamename, price, ty):
    print(game.text)
    print(price.text)
    print(ty.text)
    print("-----------------------------")

# for j in range(len(gamename)):
#     print(gamename[j].text)
#     print(price[j].text)
#     print(ty[j].text)
# for t in ty:
#     print(t.text)
# for p in price:
#     print(p.text)
# for i in gamename:
#     print(i.text)
# time.sleep(5)
