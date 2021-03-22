from selenium import webdriver
import time
import unittest
from loginpage import loginpage
from homepage import homepage

from webdriver_manager.chrome import ChromeDriverManager

class logintest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login=loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        # homepage=homepage(driver)
        # homepage.click_welcome()
        # homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()

        time.sleep(2)
    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

if __name__=='__main__':
    unittest.main()
    
    






