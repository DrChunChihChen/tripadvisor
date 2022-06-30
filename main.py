from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:/www.dunqian.tw-/chromedriver.exe')
driver.get('https://www.tripadvisor.com/Restaurant_Review-g32253-d7002210-Reviews-or15-Din_Tai_Fung-Costa_Mesa_California.html')

Friends = driver.find_element("xpath", '//*[@id="taplc_detail_filters_rr_resp_0"]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[5]/label')
driver.execute_script("arguments[0].click();", Friends)
time.sleep(3)
button2 = driver.find_element("xpath",
                                      './/*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[18]/div/div/a[2]')
driver.execute_script("arguments[0].click();", button2)
