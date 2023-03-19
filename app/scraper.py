from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from fake_useragent import UserAgent
from dataclasses import dataclass
import time

def get_user_agent():
    return UserAgent(verify_ssl=False).random


@dataclass
class Scraper:
    url: str
    endless_scroll: bool = False
    endless_scroll_time: int = 5
    driver: WebDriver = None

    def get_driver(self):
        if self.driver is None:
            user_agent = get_user_agent()
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            options.add_argument(f"user-agent={user_agent}")
            driver = webdriver.Chrome(options=options)
            self.driver = driver

        return driver
    
    def perform_endliess_scroll(self, driver=None):
        if self.driver is None:
            return
        if self.endless_scroll:
            current_heigth = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(self.endless_scroll_time)
                iter_height = driver.execute_script("return document.body.scrollHeight")
                if current_heigth == iter_height:
                    break
                current_heigth = iter_height
        return driver.page_source
    

    def get(self):
        driver = self.get_driver()
        driver.get(self.url)
        self.perform_endliess_scroll(driver=driver)
        return driver.page_source