from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import re
from frameworks import frameworks

lnk_usr = 'adityagandhi176@gmail.com'
lnk_pwd = 'adis2345890'

job_url = 'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3912824359&eBP=CwEAAAGQzVrt-WANa2p30zqt7xU90QSe8QMekFfvT33jKFmw9mGrd3siXYjKXhpQk6n6XW2-dYVGZsnNzc16cPZo9Fpa4ydW_leXTfVyupKV1c1A6b_7Rm51qfvx-gA5Ror05g3W67EBKpojqy_tPExnHYZg7XoQFfDp3uYN1On8gMtzDU5VmFiJWxXQo7xGRMILggR8HC5MpwHdZeNQ4MFdnE1mFEbIOMd450TYcfgH4W6iDmLLJK5ig-Gn5lH5bXhhh-8oRWmUWvVSwnbDK-84jNychDvYmM-5eRpA6mQF4NPzyolNA7xx_PNhWNBhFFD5rwV3FEyyODY59PGs6ZWceB0PSZ8Dk5NU1fWFLUCVs9pagBjfjrH_7bConSKA7x0R11CgEkv-pB-_XtLmbb2XI6TyHv58NuHJB4yoX7UjwI5ivEhYDdNAI6MTtIKfFGtnRmQ&refId=PqUkDhIn%2B9B7vpNQ6XgKkg%3D%3D&trackingId=3X2W7AYxxelTiaw1P6h5rQ%3D%3D'

driver = webdriver.Chrome()

def preprocess_text(txt):
    txt=re.sub(r'[^A-Za-z0-9\s]', ' ',txt)
    txt=txt.lower()
    words=txt.split()
    return words

def count_matches(text, word_array):
    process = preprocess_text(text)
    arr = [word.lower() for  word  in  word_array]
    comm = [word  for  word  in arr  if  word  in  process]
    return comm

try:
    driver.get('https://www.linkedin.com/login')

    usr_inp = driver.find_element(By.ID, 'username')
    usr_inp.send_keys(lnk_usr)
    
    pwd_inp = driver.find_element(By.ID, 'password')
    pwd_inp.send_keys(lnk_pwd)
    pwd_inp.send_keys(Keys.RETURN)
    
    time.sleep(5)
    driver.get(job_url)
    time.sleep(5) 
    job_desp = ""

    try:
        job_ele_1 = driver.find_element(By.CLASS_NAME, "jobs-description__container")
        job_html_1 = job_ele_1.get_attribute('innerHTML')
        soup_1 = BeautifulSoup(job_html_1, 'html.parser')
        job_desp_1 = ' '.join(soup_1.stripped_strings)
        job_desp += job_desp_1
    except NoSuchElementException:
        print("Element with class 'jobs-description__container' ain't not found")

    try:
        job_ele_2 = driver.find_element(By.CLASS_NAME, "job-details-segment-attribute")
        job_html_2 = job_ele_2.get_attribute('innerHTML')
        soup_2 = BeautifulSoup(job_html_2, 'html.parser')
        job_desp_2 = ' '.join(soup_2.stripped_strings)
        job_desp += " " + job_desp_2
    except NoSuchElementException:
        print("Element with class 'job-details-segment-attribute' not found")

    matches = count_matches(job_desp, frameworks)
    print("Matches:", matches)

    with open('job_description.txt', 'w', encoding='utf-8') as file:
        file.write(job_desp)

    with open('matches.js', 'w', encoding='utf-8') as file:
        file.write(f"const matches = {matches};\n")

    print("Matches have been saved to matches.js")

finally:
    driver.quit()
