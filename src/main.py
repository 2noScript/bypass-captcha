from selenium import webdriver
import os
current_directory = os.path.dirname(os.path.realpath(__file__))





driver=webdriver.Chrome()



driver.get('https://pypi.org/project/selenium/')

driver.close()