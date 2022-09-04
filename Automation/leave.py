import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLeave(unittest.TestCase):  # TEST SCENARIO

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
    
    def test_configure_work_week(self):
        browser = self.browser
        self.login()
        browser.find_element(By.XPATH,"//span[normalize-space()='Leave']").click() # klik tombol Leave
        time.sleep(3)
        browser.find_element(By.XPATH,"//span[normalize-space()='Configure']").click() #klik tombol Configure
        time.sleep(3)
        browser.find_element(By.XPATH,"//a[normalize-space()='Work Week']").click() #klik tombol Work Week
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[normalize-space()='Save']").click() #klik tombol Save
        time.sleep(3)
        
        # validasi
        text = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]").text

        self.assertIn('Configure', text)
    
    def tearDown(self): 
        self.browser.close()
    
        
if __name__ == "__main__": 
    unittest.main()