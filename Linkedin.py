#!pip install webdriver-manager #if using jupyterNotebook##############################################

import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
service = Service(ChromeDriverManager().install())
service.start()


PATH =  r"C:\Users\manu\ChromeDriver.exe"

# Define your LinkedIn login credentials
username =
password =




try:
    # Navigate to the LinkedIn login page
    browser.get('https://www.linkedin.com/uas/login')

    # Find the username and password fields and enter the credentials
    username_field = browser.find_element(By.ID, 'username')


    username_field.send_keys(username)
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the homepage to load
    time.sleep(2)

####################################send keys and enter#############################################


    # Find the search bar and enter the job title and location
    search_bar = browser.find_element(By.CSS_SELECTOR,'#global-nav-typeahead > input')
    search_bar.send_keys('Python developer')
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)
###################################Find the 'Apply' buttons for the job listings##################################
    apply_buttons = browser.find_elements_by_xpath('//button[contains(@class,"job-card__apply-button")]')

    # Loop through the 'Apply' buttons and click them
    for button in apply_buttons:
        button.click()
        time.sleep(2)
        browser.back()
        time.sleep(2)

except Exception as e:
    print(f'An error occurred: {e}')
    ###########################################logeed into linked in############################################
    ###########################################XpathVersion#######################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

driver.get("https://linkedin.com")

time.sleep(2)
username = driver.find_element(by=By.XPATH, value=("//input[@name='session_key']"))
password = driver.find_element(by=By.XPATH, value=("//input[@name='session_password']"))

time.sleep(2)
username.send_keys("alexandernefsyne@gmail.com")
password.send_keys("illithid112")
time.sleep(2)

submit = driver.find_element(by=By.XPATH, value=("//button[@type= 'submit']")).click()
time.sleep(2)

########################################message people#############################################
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=7zJ")
time.sleep(2)

message_button = driver.find_element(By.XPATH, value=("//button[@type ='message']"))

# all_buttons = driver.find_element(by=By.XPATH, value=("//*[@id='ember52']"))
    # message_button = [btn for btn in all_buttons if btn.text == "message"]

    #"//button[@data-control-name='search_srp_message']"

message_button[0].click()

browser.close()