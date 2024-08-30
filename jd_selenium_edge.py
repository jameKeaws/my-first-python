# Driver binaries need to be on your PATH, or you need to override a parameter 
# The python client will just try to run them by their names safaridriver, geckodriver, chromedriver, etc.

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

def main():
        # Chrome() > this is a class.  We are creating an instance of Chrome() class
        # Selenium client library will do a things
        # 1st it will start the chromedriver
        # 2nd it will construct a set of capabilities that are appropriate for starting a Chrome session
        # 3rd it will send capabilities as POST request to the appropriate route at the chromedriver server, 
        # so that the server can launch a browser and start a session
        # 4th it will listen for the new session request response, and wrap the session id in a nice object for us, 
        # which is the driver variable
    try:
        # driver = webdriver.Chrome()
        # Talking about the built-in driver types that we have access to in the Selenium client
        # webdriver.Edge() > The edge browser has recently undergone to use chromium under the hood
        # If you are using the newest Edge browser and newest Edge driver
        # options = webdriver.EdgeOptions()
        # options.use_chromium = True
        # driver = webdriver.Edge(options=options)
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        driver = webdriver.Edge(options=options)
        # Navigate to webpage
        driver.get('https://www.perthmint.com/')
        time.sleep(5)
    finally:
        # When we call driver.quit(), driver method is running method on itself
        # That quit method, has access to the session id which is in the driver object
        # That session id is then added to appropriate http call to chromedriver to delete the session
        driver.quit()
    
if __name__ == "__main__":
    print('This is invoked from main method of selenium_edge.py')
    main()