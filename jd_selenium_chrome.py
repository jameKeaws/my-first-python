# Driver binaries need to be on your PATH, or you need to override a parameter 
# The python client will just try to run them by their names safaridriver, geckodriver, chromedriver, etc.

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

def main():
    driver = webdriver.Chrome()
    try:
        # Navigate to webpage
        driver.get('https://www.perthmint.com/')
        time.sleep(5)
    finally:
        # When we call driver.quit(), driver method is running method on itself
        # That quit method, has access to the session id which is in the driver object
        # That session id is then added to appropriate http call to chromedriver to delete the session
        driver.quit()
    
if __name__ == "__main__":
    print('This is invoked from main method of jd_selenium_chrome.py')
    main()