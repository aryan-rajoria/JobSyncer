# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import re
import os
import subprocess
from frameworks import frameworks

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

load_dotenv('.env.local')
lnk_usr =os.getenv('LINKEDIN_USERNAME')
lnk_pwd = os.getenv('LINKEDIN_PASSWORD')

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

@app.route('/api/process', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get('jobUrl')
    print("User input received: ", user_input)
    
    if user_input is None:
        return jsonify({'error': 'No input provided'}), 400
    
    # Run your Python script with the user input
    # Here we are simulating a script execution with subprocess
        
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.linkedin.com/login')

        usr_inp = driver.find_element(By.ID, 'username')
        usr_inp.send_keys(lnk_usr)
        
        pwd_inp = driver.find_element(By.ID, 'password')
        pwd_inp.send_keys(lnk_pwd)
        pwd_inp.send_keys(Keys.RETURN)
        
        time.sleep(5)
        driver.get(user_input)
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
        return jsonify({
            'status': 200,
            'matches': matches
        })
    finally:
        driver.quit()
        return jsonify({
            'status': 401,
            'matches': matches
        })




if __name__ == '__main__':
    app.run(port=5000)
