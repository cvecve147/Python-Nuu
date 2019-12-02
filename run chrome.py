from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import identifyCode as IdCode
import time


def CodeError(
        inputpw):
    password = driver.find_element_by_xpath('//*[@id="act_pwd_txt"]')
    element = driver.find_element_by_xpath('//*[@id="captchaBox"]/img')

    element.screenshot('code.png')
    IdCode.saveKaptcha()
    code = IdCode.predictKaptcha('./imagedata')
    tempcode = ""
    for i in code:
        tempcode += str(i)
    print(tempcode)
    Codes = driver.find_element_by_xpath(
        '//*[@id="baseContent_cph_confirm_txt"]')
    Codes.send_keys(tempcode)

    password.send_keys(inputpw)
    if(len(driver.find_elements_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]'))):
        if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '驗證碼錯誤'):
            print("Code Error")
            CodeError(inputpw)

    return True


def logins(inputac,
           inputpw):

    chrome_options = Options()
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://eap10.nuu.edu.tw/Login.aspx?logintype=S")
    driver.implicitly_wait(10)  # 等待最多10秒
    account = driver.find_element_by_xpath(
        '//*[@id="baseContent_cph_act_id_txt"]')
    password = driver.find_element_by_xpath('//*[@id="act_pwd_txt"]')
    element = driver.find_element_by_xpath('//*[@id="captchaBox"]/img')

    element.screenshot('code.png')
    IdCode.saveKaptcha()
    code = IdCode.predictKaptcha('./imagedata')
    tempcode = ""
    for i in code:
        tempcode += str(i)
    print(tempcode)
    Codes = driver.find_element_by_xpath(
        '//*[@id="baseContent_cph_confirm_txt"]')
    Codes.send_keys(tempcode)

    account.send_keys(inputac)
    password.send_keys(inputpw)
    login = len(driver.find_elements_by_xpath(
        '//*[@id="baseContent_cph_mainContent_cph_img_btn"]'))
    if(login <= 0):
        if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '帳號或密碼錯誤!'):
            return False
        if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '驗證碼錯誤'):
            print("Code Error")
            CodeError(inputpw)
            return True
    else:
        return True


def getData():
    print("Get Data")
    driver.get(
        "https://eap10.nuu.edu.tw/S0100/S0132/S01320901.aspx?sys_id=S00&sys_pid=S01320901")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath(
        '//*[@id="baseContent_cph_mainContent_cph_serach_btn"]').click()

    driver.implicitly_wait(5)
    time.sleep(2)
    driver.switch_to.frame(0)
    count = driver.find_elements_by_id('clsname1-0')
    # for i in driver.find_elements_by_xpath('//*[@id="clsname1-0"]'):
    #     print(i.text)
    for i in range(0, len(count)):
        myclass = driver.find_element_by_xpath(
            '/html/body/div/div/div['+str(27+i*7)+']')
        classname = driver.find_element_by_xpath(
            '/html/body/div/div/div['+str(28+i*7)+']')
        classtime = driver.find_element_by_xpath(
            '/html/body/div/div/div['+str(31+i*7)+']')
        # print(myclass.text, end="\t")
        # print(classname.text, end="\t")
        classtime = classtime.text.replace("\n", "")
        classtime = classtime.replace("  ", " ")
        classtime = classtime.replace("  ", " ")
        classtime = classtime.replace("  ", " ")
        print(classtime)
    # classtime = driver.find_element_by_xpath(
    #     '//*[@id="scrperiod1-0"]')
    driver.close()


if __name__ == '__main__':
    inputac = 'U0633126'
    fp = open('password.txt', 'r+')
    inputpw = fp.readline()
    fp.close()
    status = logins(inputac, inputpw)
    if(status):
        print("登入成功")
        getData()
    else:
        print("登入失敗")
        driver.close()
