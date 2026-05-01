import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://reg.thonburi-u.ac.th/registrar/login.asp")
       
        Acc_btn = driver.find_element(By.XPATH, '//*[@id="c-p-bn"]' )
        driver.execute_script("arguments[0].click();", Acc_btn)
        username_input = driver.find_element(By.XPATH, "//*[@id='f_uid']")
        password_input = driver.find_element(By.XPATH, "//*[@id='f_pwd']")
        login_button = driver.find_element(By.XPATH, "//input[@type='SUBMIT']")

       
        username_input.send_keys("6601103071016")
        password_input.send_keys("6601103071016")
        login_button.click()

        self.assertIn("มหาวิทยาลัยธนบุรี", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()