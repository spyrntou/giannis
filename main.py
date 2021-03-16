import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re

class database:
    def bd(data):
        print(data)



class testcrawler:
    def test():
        options = webdriver.FirefoxOptions()
        #  options.add_argument('-headless')
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "text/plain,application/zip, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml")
        driver = webdriver.Firefox(firefox_profile=profile,
                                   executable_path=r'C:/Users/spyrosn/PycharmProjects/giannis/driver/geckodriver.exe',
                                   firefox_options=options)
        base_url = "https://www.in.gr/"
        driver.get(base_url)
        #WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="ΑΠΟΔΟΧΗ"]'))).click()
        WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="ΑΠΟΔΟΧΗ"]'))).click()
        data = driver.page_source
        i = driver.find_element_by_xpath('//div[@class="latest-news"]/ul/li/a')
        print(i.get_attribute('outerHTML'))
        print(i.get_attribute("href"))
        driver.quit()
        database.bd(i)

if __name__ == "__main__":
    p = testcrawler
    p.test()
