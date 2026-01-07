from Base.InitiateDriver import startBrowser,closeBroswser
def test_LoginInvalid_Data():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='email']").send_keys("as==")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("Uman")
    driver.find_element('link text','Create new account').click()
    closeBroswser()