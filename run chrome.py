from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import identifyCode as IdCode
import time
import mysql.connector
from mysql.connector import Error
import re
import sys


def insert(account, classname, teacher, week, time):
    try:
        # 連接 MySQL/MariaDB 資料庫
        connection = mysql.connector.connect(
            host='localhost',          # 主機名稱
            database='school timetable',  # 資料庫名稱
            user='root',        # 帳號
            password='root')  # 密碼

        # 新增資料
        sql2 = "SELECT * FROM school WHERE account =%s and class=%s and  teacher=%s and week=%s and time=%s"
        new_data = (account, classname, teacher, week, time)
        cursor = connection.cursor()
        cursor.execute(sql2, new_data)
        myresult = cursor.fetchall()
        if(myresult == []):
            sql = "INSERT INTO school (account, class, teacher, week, time) VALUES (%s, %s, %s,%s,%s);"
            new_data = (account, classname, teacher, week, time)
            cursor = connection.cursor()
            cursor.execute(sql, new_data)

        # 確認資料有存入資料庫
        connection.commit()

    except Error as e:
        print("資料庫連接失敗：", e)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


def logins(inputac,
           inputpw):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
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
    password.send_keys("\n")
    login = len(driver.find_elements_by_xpath(
        '//*[@id="baseContent_cph_mainContent_cph_img_btn"]'))
    if(login <= 0):
        if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '帳號或密碼錯誤!'):
            return False
        if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '驗證碼錯誤'):
            print("Code Error")
            fo = open("opened2.txt", "r+")
            inputsucc = fo.readline()
            fo.close()
            fo = open("opened2.txt", "w+")
            inputsucc = int(inputsucc)
            inputsucc += 1
            fo.write(str(inputsucc))
            fo.close()
            while True:
                password = driver.find_element_by_xpath(
                    '//*[@id="act_pwd_txt"]')
                element = driver.find_element_by_xpath(
                    '//*[@id="captchaBox"]/img')

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
                password.send_keys("\n")

                if(len(driver.find_elements_by_xpath(
                        '//*[@id="baseContent_cph_mainContent_cph_img_btn"]'))):
                    return True

                if(len(driver.find_elements_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]'))):
                    if(driver.find_element_by_xpath('//*[@id="jGrowl"]/div[2]/div[2]').text == '驗證碼錯誤'):
                        print("Code Error")
                        fo = open("opened2.txt", "r+")
                        inputsucc = fo.readline()
                        fo.close()
                        fo = open("opened2.txt", "w+")
                        inputsucc = int(inputsucc)
                        inputsucc += 1
                        fo.write(str(inputsucc))
                        fo.close()
                        continue
                return True
    else:
        return True


def getData(account):
    print("Get Data")
    driver.get(
        "https://eap10.nuu.edu.tw/S0100/S0132/S01320901.aspx?sys_id=S00&sys_pid=S01320901")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath(
        '//*[@id="baseContent_cph_mainContent_cph_serach_btn"]').click()

    driver.find_elements_by_xpath(
        '//*[@id="bobjid_1575905169322_iframe"]')
    driver.switch_to.frame(0)

    classname = driver.find_elements_by_xpath('// *[@id="subname1-0"]')
    classtime = driver.find_elements_by_xpath('//*[@id="scrperiod1-0"]')
    classnamelist = []
    classtimelist = []
    #

    for i in classname:
        classnamelist.append(i.text)
    for i in classtime:
        cleartime = i.text.replace("\n", "")
        cleartime = cleartime.replace("  ", " ")
        cleartime = cleartime.replace("  ", " ")
        cleartime = cleartime.replace("  ", " ")
        classtimelist.append(cleartime)

    for i in range(0, len(classnamelist)):
        regex(account, classnamelist[i], str(classtimelist[i]))
        # print(classnamelist[i], classtimelist[i])
    # id 自己產生編號
    # acount 帳號
    # class 課程名稱
    # teacher 老師
    # week 星期
    # time 上課時間


def regex(account, classname, classtime):
    alltime = re.findall(
        "\([一二三四五六]\)0[0-9]-0[0-9]|\([一二三四五六]\)0[0-9]", classtime)
    for i in alltime:
        week = re.findall("\([一二三四五六]\)|\([一二三四五六]\)", i)
        time = re.findall("0[0-9]-0[0-9]|0[0-9]", i)
        teacher = classtime.split(" ")
        teacher = teacher[-1]
        desh = "-"

        for j in time:
            try:
                j.index(desh)
            except (ValueError):
                print(account, classname, teacher, week[0], time[0])
                insert(account, classname, teacher, week[0], int(time[0]))
            else:
                times = j.split("-")
                for k in range(int(times[0]), int(times[1])+1):
                    print(account, classname, teacher, week[0], k)
                    insert(account, classname, teacher, week[0], k)


if __name__ == '__main__':
    start = time.time()
    inputac = sys.argv[1]
    inputpw = sys.argv[2]
    fo = open("opened.txt", "r+")
    inputsucc = fo.readline()
    fo.close()
    fo2 = open("opened2.txt", "r+")
    inputsucc2 = fo2.readline()
    fo2.close()
    print("目前準確度：", str(1-int(inputsucc2)/int(inputsucc)))
    fo = open("opened.txt", "w+")
    inputsucc = int(inputsucc)
    inputsucc += 1
    fo.write(str(inputsucc))
    fo.close()
    status = logins(inputac, inputpw)
    if(status):
        print("登入成功")
        # getData(inputac)
    else:
        print("登入失敗")

    driver.close()
    driver.quit()
    end = time.time()
    elapsed = end - start
    print("Time taken: ", elapsed, "seconds.")
    # ivy0920265978
    # regex("資訊管理實務專題(一) - 未排教室 張朝旭生涯發展與規劃 (一)03-04 K2-204 高淑芳系統分析與設計 (一)06-07 C1-615 (四)03 C1-615 陳宇佐人工智慧程式設計 (二)02-04 C1-607 曾筱珽網路廣告 (三)02-03 C1-615 (四)02 C1-602 楊宗珂資料庫系統實務 (三)07-09 C1-607 陳士杰戲劇的哲學批判 (四)05-06 K2-103 陳俊宇商用英文書信實務(一) (四)07-08 H1-706 程小芳")

# 102 63
# 100 28
# 868 290
# 1005 330
# 1035 204
