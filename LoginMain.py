from selenium import webdriver
import unittest
from Test.POMDemo.Pages.loginPage import LoginPage
from Test.POMDemo.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed ping")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Parallels/PycharmProjects/Project_test/Test/driver/report'))
