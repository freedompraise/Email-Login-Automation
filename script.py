from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from dotenv import load_dotenv
import os
load_dotenv()


usernameStr = 'praise.dike@eng.uniben.edu'
passwordStr = os.getenv('PASSWORD')

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_xpath("//button[contains(text(), 'Next')]")
nextButton.click()

password = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.NAME, 'Passwd')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_xpath("//button[contains(text(), 'Next')]")
nextButton.click()