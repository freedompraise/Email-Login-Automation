from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from dotenv import load_dotenv
import os
load_dotenv()


usernameStr = 'praise.dike@eng.uniben.edu'
passwordStr = os.getenv('PASSWORD')

browser = webdriver.Chrome()
browser.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')
