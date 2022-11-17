from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import datetime, date

import time, os, shutil, re, traceback, parameters, csv, os.path, time


# Functions 
def search_and_send_request(keywords, till_page):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.headless=True
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://www.linkedin.com/login')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(parameters.linkedin_username)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(parameters.linkedin_password)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]'))).click()
    time.sleep(5)
    try:
        input_2fa = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input__phone_verification_pin"]')))
        submit_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="two-step-submit-button"]')))
        while True:
            code_2fa=input("2fa code found. Please type it on the webdriver.") 
            input_2fa.send_keys(code_2fa)
            submit_button.click()
            if input_2fa:
                print('please type correct code') 
            else:
                break
    except:
        pass
    for page in range(1, till_page + 1):
        print('\nINFO: Checking on page %s' % (page))
        query_url = 'https://www.linkedin.com/search/results/people/?keywords=' + keywords + '&origin=GLOBAL_SEARCH_HEADER&page=' + str(page)
        driver.get(query_url)
        linkedin_urls = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reusable-search__result-container')))
        print('INFO: %s connections found on page %s' % (len(linkedin_urls), page))
        profile_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.entity-result__item')))
        time.sleep(5)
        for element in profile_list:
            name=element.find_element(By.CSS_SELECTOR,".entity-result__title-text .app-aware-link span[aria-hidden]").text
            job=element.find_element(By.CSS_SELECTOR,"div.entity-result__primary-subtitle").text      
            location=element.find_element(By.CSS_SELECTOR,"div.entity-result__secondary-subtitle").text
            try:
                connection = element.find_element(By.CSS_SELECTOR,".entity-result__actions span")
            except:
                connection = element.find_element(By.CLASS_NAME,"artdeco-button__text")
            custom_message=str("Hi %s,\n\n" % (str(name).split(" ")[0])) +  parameters.custom_message
            try:
                if connection.text == 'Connect':
                    try:
                        coordinates = connection.location_once_scrolled_into_view # returns dict of X, Y coordinates
                        driver.execute_script("window.scrollTo(%s, %s);" % (coordinates['x'], coordinates['y']))
                        time.sleep(5)
                        connection.click()
                        time.sleep(5)
                        if driver.find_elements(By.CLASS_NAME,'artdeco-button--primary')[0].is_enabled():
                            driver.find_elements(By.CLASS_NAME,'artdeco-button--secondary')[0].click()                  
                            driver.find_element(By.ID,'custom-message').send_keys(custom_message)                       
                            driver.find_elements(By.CLASS_NAME,'artdeco-button--primary')[0].click()
                            writer.writerow((name, job, location, "Request sent on", str(date.today().strftime("%B %d, %Y"))))
                            print("SENT: %s" % (name))
                        else:
                            driver.find_element(By.ID,'email').send_keys(parameters.linkedin_username)
                            driver.find_elements(By.CLASS_NAME,'artdeco-button--secondary')[0].click() 
                            driver.find_element(By.ID,'custom-message').send_keys(custom_message)
                            driver.find_elements(By.CLASS_NAME,'artdeco-button--primary')[0].click()
                            writer.writerow((name, job, location, "Request sent on", str(date.today().strftime("%B %d, %Y"))))
                            print("CANT: %s" % (name))
                    except Exception as e:
                        driver.find_element(By.CLASS_NAME,'artdeco-modal__dismiss')[0].click()
                        writer.writerow((name, job, location))
                        print('ERROR: %s' % (e))
                    time.sleep(5)
                elif connection.text == 'Pending':
                    writer.writerow((name, job, location))
                    print("PENDING: %s" % (name))
            except:
                writer.writerow((name, job, location))
                print("ERROR: You might have reached limit")


if __name__ == '__main__':
    #VARIABLES
    username=parameters.linkedin_username
    password=parameters.linkedin_password
    till_page=parameters.till_page
    keywords=parameters.keywords
    
    # CSV file loging
    file_name = parameters.file_name
    file_exists =  os.path.isfile(file_name)
    writer = csv.writer(open(file_name, 'a'))
    if not file_exists: 
        writer.writerow(('Name', 'Job position', 'Location'))
        
    # Search
    search_and_send_request(keywords, till_page, writer)

    
     