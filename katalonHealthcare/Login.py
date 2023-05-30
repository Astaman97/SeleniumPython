import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_failed_login(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "btn-login").click()
        error_message = driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[1]/p[2]').text
        self.assertIn("Login failed! Please ensure the username and password are valid.", error_message)

    def test_success_login(self): #test cases 2
        baseUrl = "https://katalon-demo-cura.herokuapp.com"
        driver = self.browser
        driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()
        url = driver.current_url
        self.assertIn(url, baseUrl + "/#appointment")

if __name__ == '__main__':
    unittest.main()