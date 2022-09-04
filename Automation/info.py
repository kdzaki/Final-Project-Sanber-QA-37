import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestInfo(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def login(self): 
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)
    
    def test_change_nickname(self): 
        # steps
        browser = self.browser #buka web browser
        self.login()
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() # klik menu My Info
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("SanberQA") #add nickname
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click() # klik tombol Save
        time.sleep(3)

        # validasi
        text = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertIn('PIM', text)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()