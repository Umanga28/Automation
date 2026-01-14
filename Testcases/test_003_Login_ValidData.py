#from Base.InitiateDriver import startBrowser,closeBroswser
from selenium.webdriver import Chrome

def test_LoginInvalid_Data():
    driver=Chrome()
    driver.get("https://facebook.com/login")
    driver.find_element('xpath',"//input[@name='email']").send_keys("as==")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("Uman")
    driver.find_element('link text','Create new account').click()
    #closeBrowser()
    driver.close()
