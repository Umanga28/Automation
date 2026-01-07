from Base.InitiateDriver import startBrowser,closeBroswser
def test_ValidateRegistration():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='firstname']").send_keys('Umanga')
    driver.find_element('xpath',"//input[@name='lastname']").send_keys('Yogi')
    closeBroswser()
    