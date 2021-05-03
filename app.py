from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import openpyxl as excel
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)



msg = "Hello World!"



def readContacts(fileName):
    number = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']

    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        number.append(contact)
    return number
customers = readContacts("customers.xlsx")



for i in customers:
    sendmsg = "+" + i
    search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
    search_box.send_keys(sendmsg)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(5)


contact = "+919360724035"
driver.get('https://wa.me/{}'.format(contact))
contChat = driver.find_element_by_xpath("//*[@id='action-button']")
time.sleep(5)

driver.quit()