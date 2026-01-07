from selenium.webdriver import Chrome,Edge,Firefox
from Library.ConfigReader import configRead
def startBrowser():
    global driver
    if configRead('Details','browser')=='Chrome':
        driver=Chrome()
    elif configRead('Details','browser')=='edge':
        driver=Edge()
    else:
        driver=Firefox()
    driver.get(configRead('Details','APP_URL'))
    driver.maximize_window()
    return driver

def closeBroswser():
    driver.close()