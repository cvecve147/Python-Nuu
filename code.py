from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def logins():

    chrome_options = Options()
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://eap10.nuu.edu.tw/Login.aspx?logintype=S")
    driver.implicitly_wait(10)  # 等待最多10秒
    element = driver.find_element_by_xpath('//*[@id="captchaBox"]/img')
    element.screenshot('code.png')

    driver.close()


if __name__ == '__main__':
    status = logins()
