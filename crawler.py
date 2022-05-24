import os

from selenium import webdriver
from selenium.common.exceptions import *

class Crawler:

    def __init__(self):
        work_dir = os.getcwd()
        
        driver_path = '\\'.join([work_dir, 'firefox-driver', 'geckodriver.exe'])
        search_engine = 'https://google.com.br'
        looking_for = 'JBL Quantum One'

        options.headless = True

        browser = webdriver.Firefox(executable_path = driver_path)

    def open_url(self, url):
        browser.get(url)

    def search(self):
        search_bar = browser.find_element_by_name('q')
        search_bar.send_keys([search_item, Keys.RETURN])