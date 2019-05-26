"""U-Pass Auto Completer (upass.py)

This script allows university students in Vancouver to renew their U-Pass automatically.

This tool requires an additional Python script (init.py) that creates a textfile that this script reads.

This script requires that 'selenium' be installed within the Python environment you are running this script to.

"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions 
import time
import sys

#Tries to open info.txt, if doesn't exist throws error.
try:
    f = open("info.txt", "r")
    school = int(f.readline())
    email = f.readline()
    pw = f.readline()
except:
    print("Please run init.py before this script.")
    sys.exit()

#Only chrome right now
#TODO: Other browser support.
driver = webdriver.Chrome("drivers\chromedriver.exe")
wait = WebDriverWait(driver, 10)

driver.set_page_load_timeout(10)
driver.get("https://upassbc.translink.ca/")

#U-Pass initial page
select_school = Select( driver.find_element_by_id("PsiId") )
select_school.select_by_index(school)
driver.find_element_by_id("goButton").click()

#School portal page, depends on what user put in text file.
if (school == 9 or school == 2 or school == 5): #sfu, kpu, bcit
    user_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("username")) 
    password_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("password")) 
    submit_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("submit"))  
    user_element.send_keys(email)
    password_element.send_keys(pw)
    try:
        submit_element.click()
    except exceptions.StaleElementReferenceException:
        pass
elif (school == 4 or school == 7): #ubc, ecarr
    user_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("username")) 
    password_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("password")) 
    submit_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("_eventId_proceed"))  
    user_element.send_keys(email)
    password_element.send_keys(pw)
    try:
        submit_element.click()
    except exceptions.StaleElementReferenceException:
        pass
elif (school == 1 or school == 3, school == 10): #douglas, nicola, vcc
    user_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("ctl00_ContentPlaceHolder1_UsernameTextBox")) 
    password_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("ctl00_ContentPlaceHolder1_PasswordTextBox")) 
    submit_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton"))  
    user_element.send_keys(email)
    password_element.send_keys(pw)
    try:
        submit_element.click()
    except exceptions.StaleElementReferenceException:
        pass
elif (school == 6 or school == 8): #capu, langara
    user_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("userNameInput")) 
    password_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("passwordInput")) 
    submit_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("submitButton"))  
    user_element.send_keys(email)
    password_element.send_keys(pw)
    try:
        submit_element.click()
    except exceptions.StaleElementReferenceException:
        pass


#clicks everything on the page that has tag input but works...
checkboxes = wait.until(lambda driver: driver.find_elements_by_tag_name("input"))

for cb in checkboxes:
    try:
        cb.click()
    except exceptions.ElementNotVisibleException:
        print("element not interactable")
        pass


time.sleep(4)

driver.quit()
