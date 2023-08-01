# Import Modules

from selenium import webdriver
# import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

with open('ip.txt') as f:
    datafile = f.readlines()

found = False

def check(ip):
    global found
    for line in datafile:
        if ip in line:
             found = True


def run(propro):
        # chrome_options = uc.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=socks5://52.157.88.150:80')
        chrome_options.add_argument(f'--proxy-server={propro}')
        # driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        try:
            driver.get("https://gitopia.com/login")
            # get element
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/button[2]")
            element.click()
            pw = driver.find_element(By.XPATH, "//input[@name='wallet_password']")
            con_pw = driver.find_element(By.XPATH, "//input[@name='wallet_confirm_password']")
            pw.send_keys("kopisaja")
            con_pw.send_keys("kopisaja")
            create = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[4]/div[3]/button[1]")
            create.click()
            try:
                element = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "reapop__notification-message"))
                ).text
                print(element)
                if element == "Unable to reach faucet":
                    print("this ip already claimed: " + propro)
                    file_object.write("\n" + propro)
                    driver.quit()
                else:
                    print("faucet ready")
                    time.sleep(7)
                    sendDrop = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/button[1]")
                    sendDrop.click()
                    time.sleep(2)
                    send = driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]")
                    send.click()
                    time.sleep(2)
                    address = driver.find_element(By.XPATH, "//input[@name='toAddress']")
                    jml = driver.find_element(By.XPATH, "//input[@name='amount']")
                    address.send_keys("")
                    jml.send_keys("9.99")
                    sendAct = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
                    sendAct.click()
                    time.sleep(15)
                    driver.quit()
                    print("claim done for ip: "+propro)
                    file_object.write("\n" + propro)
            finally:
                print("done")
        except WebDriverException:
            print("this ip error: "+propro)
            file_object.write("\n" + propro)
            driver.quit()
        except NoSuchElementException:
            print("this ip error: "+propro)
            file_object.write("\n" + propro)
            driver.quit()

file_object = open('ip.txt', 'a')


def mulai():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        #driver1 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
        driver1 = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver1.get("https://www.sslproxies.org/")
        tbody = driver1.find_element_by_tag_name("tbody")
        cell = tbody.find_elements_by_tag_name("tr")
        for column in cell:
            # print(column.text)
            column = column.text.split(" ")
            proxy = column[0] + ":" + column[1]
            print(proxy)
            try:
                run(proxy)
            except NoSuchElementException:
                print("this ip error: " + proxy)
                time.sleep(2)
            if column == cell[-1]:
                mulai()


mulai()
file_object.close()












#Proxy Connection

# print(colored('Getting Proxies from graber...','green'))
# time.sleep(2)
# proxy = {"http": "http://"+ column[0]+":"+column[1]}
# print(proxy)
# url = 'https://mobile.facebook.com/login'
# r = requests.get(url,  proxies=proxy)
# print("")
# print(colored('Connecting using proxy' ,'green'))
# print("")
# sts = r.status_code
# print(sts)
# proxy = column[0]+":"+column[1]
# ip = column[0]
# options = webdriver.ChromeOptions()
# #options.add_argument('headless')
# # options.add_argument(f'--proxy-server=socks5://{proxy}')
# # options.AddArgument($"--proxy-server=socks5://{proxy}");
# options.add_argument(f'--proxy-server=socks5://{ip}')
# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), crhome_options=options)
# browser.get("https://ipsaya.com")
# #element = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/button[2]")
# #print(element)
