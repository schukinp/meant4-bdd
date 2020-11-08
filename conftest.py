from selenium import webdriver
from selene import config, browser


driver = webdriver.Chrome()
config.timeout = 10
browser.set_driver(driver)

base_url = 'http://automationpractice.com/'
