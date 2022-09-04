import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestTime(unittest.TestCase):  # TEST SCENARIO

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
    
    def test_a_addcust_success(self):
        browser = self.browser
        self.login()
        browser.find_element(By.XPATH,"//span[normalize-space()='Time']").click() # klik tombol Time
        time.sleep(3)
        browser.find_element(By.XPATH,"//span[normalize-space()='Project Info']").click() #klik tombol Project Info
        time.sleep(3)
        browser.find_element(By.XPATH,"//a[normalize-space()='Customers']").click() #klik tombol Customers
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[normalize-space()='Add']").click() #klik tombol Add
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("Trial Customer37")
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[normalize-space()='Save']").click() #klik tombol Save
        time.sleep(3)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]").text
        
        self.assertIn('Time', text_atas)
    
    def test_b_addcust_failed(self):
        browser = self.browser
        self.login()
        browser.find_element(By.XPATH,"//span[normalize-space()='Time']").click() # klik tombol Time
        time.sleep(3)
        browser.find_element(By.XPATH,"//span[normalize-space()='Project Info']").click() #klik tombol Project Info
        time.sleep(3)
        browser.find_element(By.XPATH,"//a[normalize-space()='Customers']").click() #klik tombol Customers
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[normalize-space()='Add']").click() #klik tombol Add
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("Trial Customer37")
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[normalize-space()='Save']").click() #klik tombol Save
        time.sleep(3)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span").text
        
        self.assertIn('Already exists', text_atas)
    
    def tearDown(self): 
        self.browser.close()
    
        
if __name__ == "__main__": 
    unittest.main()