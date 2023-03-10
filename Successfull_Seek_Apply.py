import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
 # def teardown_method(self, method):
   # self.driver.quit()
  
  def test_applyonseek(self):
    # Test name: applyonseek
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.seek.co.nz/")
    # 2 | setWindowSize | 752x824 | 
    self.driver.set_window_size(752, 824)
    # 3 | type | id=keywords-input | python developer
    self.driver.find_element(By.ID, "keywords-input").send_keys("python developer")
    # 4 | sendKeys | id=keywords-input | ${KEY_ENTER}
    self.driver.find_element(By.ID, "keywords-input").send_keys(Keys.ENTER)
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | click | css=.yvsb870:nth-child(2) > .yvsb870:nth-child(1) > div:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".yvsb870:nth-child(2) > .yvsb870:nth-child(1) > div:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1)").click()
    # 7 | click | css=.sticky > .yvsb870 > .yvsb870:nth-child(1) > .yvsb870 | 
    self.driver.find_element(By.CSS_SELECTOR, ".sticky > .yvsb870 > .yvsb870:nth-child(1) > .yvsb870").click()
    # 8 | click | css=.\_12ytqjg0:nth-child(1) > .\_1kzqo4e20 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_12ytqjg0:nth-child(1) > .\\_1kzqo4e20").click()
    # 9 | click | id=question-AUS_Q_2_V_5_0 | 
    self.driver.find_element(By.ID, "question-AUS_Q_2_V_5_0").click()
    # 10 | click | css=.\_12ytqjg0:nth-child(1) > .\_1kzqo4e20 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_12ytqjg0:nth-child(1) > .\\_1kzqo4e20").click()
    # 11 | runScript | window.scrollTo(0,203.1999969482422) | 
    self.driver.execute_script("window.scrollTo(0,203.1999969482422)")
    # 12 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 13 | click | css=.\_1kzqo4eeq > .\_12ytqjg0 > .\_12ytqjg0 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1kzqo4eeq > .\\_12ytqjg0 > .\\_12ytqjg0").click()
    # 14 | click | css=.\_1kzqo4ey | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1kzqo4ey").click()
    # 15 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 16 | click | css=.\_1kzqo4ey | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1kzqo4ey").click()
  
