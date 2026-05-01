from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time         

from PIL import Image
import io

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# เปิดหน้าเว็บด้วย Chrome   

# driver = webdriver.Chrome()
# driver.get('https://th.wikipedia.org/wiki/กูเกิล')
# print(driver.current_url) # url หน้าเว็บ
# print(driver.title) # ชื่อหน้าเว็บ
# print(len(driver.page_source)) # โค้ด html ของหน้าเว็บ (ในที่นี้ขอดูแค่ความยาวของหน้า)
# # driver.quit()
# time.sleep(10)

# เปลี่ยนหน้าเว็บ

# driver = webdriver.Chrome()
# driver.get('https://www.google.co.th')
# print(driver.title)
# time.sleep(10)
# driver.get('https://th.wikipedia.org')
# time.sleep(10)
# print(driver.title)
# driver.back()
# time.sleep(10)
# print(driver.title)
# driver.forward()
# print(driver.title)
# time.sleep(10)  
# driver.quit()

# บันทึกหน้าเว็บ

# driver = webdriver.Chrome()
# driver.get('https://th.wikipedia.org/wiki/%E0%B9%82%E0%B8%8B%E0%B8%9A%E0%B8%B0')
# driver.save_screenshot('phapnacho.png')
# time.sleep(10)

# บันทึกเป็นไฟล์ทันทีแล้วเก็บไว้ในตัวแปร
# Selenium: ถ่ายภาพหน้าจอและรับค่าเป็นไบต์
# io.BytesIO: นำไบต์นั้นมาใส่ในถังพัก BytesIO เพื่อทำให้เป็น "ไฟล์จำลอง"
# PIL.Image: สั่ง Image.open(BytesIO(...)) เพื่อเปิดไฟล์จำลองนั้นขึ้นมาเป็นวัตถุรูปภาพสำหรับประมวลผลต่อไป 

# driver = webdriver.Chrome()
# driver.get('https://th.wikipedia.org/wiki/อูดง')
# png = driver.get_screenshot_as_png()
# Image.open(io.BytesIO(png)).show()

# การเปิดเว็บโดยไม่ต้องแสดงหน้าต่างให้เห็น (headless)

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--window-size=1280,1080')
# driver = webdriver.Chrome(options=options)
# driver.get('https://th.wikipedia.org/wiki/โซบะ')
# driver.save_screenshot('phapnach.png')
# driver.quit()

# การกำหนดความกว้างและความสูงของหน้าต่าง

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--window-size=1280,1080')
# driver = webdriver.Chrome(options=options)
# driver.get('https://th.wikipedia.org/wiki/เทริยากิ')
# driver.save_screenshot('phapnac.png')
# driver.quit()

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver.get('https://th.wikipedia.org/wiki/เนื้อมัตสึซากะ')
# driver.set_window_size(1280,1080)
# driver.save_screenshot('phapnacho1.png')
# driver.quit()

# การสั่งรันจาวาสคริปต์ในหน้าต่าง

# driver = webdriver.Chrome()
# driver.get('https://google.co.th?hl=th')
# driver.set_window_size(580,310)
# kwang = driver.execute_script("return window.outerWidth;")
# sung = driver.execute_script("return window.outerHeight;")
# driver.execute_script('alert("กว้าง = %d, สูง =%d");'%(kwang,sung))
# time.sleep(10)

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# driver.get('https://th.wikipedia.org/w/index.php?title=พิเศษ:ล็อกอิน')
# width = driver.execute_script("return document.body.scrollWidth;")
# height = driver.execute_script("return document.body.scrollHeight;")
# driver.set_window_size(width,height)
# driver.execute_script("document.body.style.overflow = 'hidden';")
# driver.save_screenshot('phapnacho2.png')
# driver.quit()

# การค้นหาส่วนที่ต้องการในหน้าต่างจากแอตทริบิวต์ name ของแท็ก

# driver = webdriver.Chrome()
# driver.get('https://th.wikipedia.org/w/index.php?title=พิเศษ:ล็อกอิน')
# pum = driver.find_element('id','wpLoginAttempt')
# print(pum.size) # ขนาดของแท็ก
# print(pum.location) # ตำแหน่งของแท็ก
# print(pum.tag_name) # ชนิดแท็ก
# print(pum.text) # ข้อความในแท็ก

# driver = webdriver.Chrome()
# driver.get('https://www.google.co.th?hl=th')
# q = driver.find_element('name','q')
# print(q.size)
# print(q.location)
# print(q.tag_name)
# print(q.get_attribute('class'))
# print(q.get_attribute('type'))
# print(q.get_attribute('title'))

#การพิมพ์ข้อความในช่องกรอกข้อความ

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--window-size=400,400')
# driver = webdriver.Chrome(options=options)
# driver.get('https://th.wikipedia.org/w/index.php?title=พิเศษ:ล็อกอิน')
# wpname = driver.find_element('id','wpName1')
# wpname.send_keys('ฉันเองไงล่ะ')
# driver.save_screenshot('phapnacho3.png')
# driver.quit()

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--window-size=1280,1080')
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.google.com/webhp?hl=th&sa=X&ved=0ahUKEwiysNrHsu-SAxUm8TgGHVbWGj8QPAgJ')
# q = driver.find_element('name','q')
# q.send_keys('ไพธอน')
# driver.save_screenshot('phapnacho4.png')
# q.send_keys(Keys.ENTER)
# driver.save_screenshot('phapnach5.png')
# driver.quit()

driver = webdriver.Chrome()
driver.get('https://www.google.co.th?hl=th')
q = driver.find_element('name','q')
q.send_keys('ใครมา')
# q.send_keys(Keys.SHIFT+Keys.LEFT+Keys.LEFT) # ลากคลุมไปทางซ้าย ๒ ช่อง
q.send_keys(Keys.CONTROL+'a') # ลากคลุมข้อความทั้งหมด
q.send_keys(Keys.CONTROL+'c') # คัดลอกข้อความที่ลากคลุม
# q.send_keys(Keys.DELETE) # ลบข้อความทั้งหมด
# q.send_keys('ไม่')
q.send_keys(Keys.CONTROL+'v') # แปะข้อความ
time.sleep(5)