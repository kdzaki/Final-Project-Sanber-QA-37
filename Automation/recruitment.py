import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRec(unittest.TestCase):  # TEST SCENARIO

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
    
    def test_add_candidates(self): 
        # steps
        browser = self.browser #buka web browser
        self.login()
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span").click() # klik menu Recruitment
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik Add
        time.sleep(3)
        browser.find_element(By.NAME,"firstName").send_keys("Pelamar") #isi First Name
        time.sleep(1)
        browser.find_element(By.NAME,"middleName").send_keys("Kerja") #isi Middle Name
        time.sleep(1)
        browser.find_element(By.NAME,"lastName").send_keys("Baru37") #isi Last Name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("newcandidate37@sanber.com") #isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click() #klik tombol Save
        time.sleep(3)
        
        # validasi
        text_atas = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertIn('Recruitment', text_atas)
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()