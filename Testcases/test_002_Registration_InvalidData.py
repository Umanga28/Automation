from Base.InitiateDriver import startBrowser,closeBroswser
from Library.ConfigReader import ElementsRead
def test_InvalidateRegistration():
    driver=startBrowser()
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys("Umanga")
    #driver.find_element('name','lastname').send_keys("123")
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys("Yogi")
    #driver.find_element('name','birthday_month').send_keys("September")
    driver.find_element('name',ElementsRead('Registration','birth_month')).send_keys("September")
    #driver.find_element('name','birthday_day').send_keys("13")
    driver.find_element('name',ElementsRead('Registration','birth_date')).send_keys("13")
    #driver.find_element('name','birthday_year').send_keys("2003")
    driver.find_element('name',ElementsRead('Registration','birth_year')).send_keys("2003")
    #driver.find_element('xpath',"//input[@value='1']").click()
    driver.find_element('xpath',ElementsRead('Registration','a')).click()
    #driver.find_element('xpath',"//input[@name='reg_email__']").send_keys("9809569428")
    driver.find_element('name',ElementsRead('Registration','email')).send_keys("9809569428")
    #driver.find_element('xpath',"//input[@aria-label='New password']").send_keys("Umanga@1234")
    driver.find_element('name',ElementsRead('Registration','password')).send_keys("Umanga@1234")
    #driver.find_element('xpath',"//button[@name='websubmit']").click()
    driver.find_element('xpath',ElementsRead('Registration','submit')).click()
    closeBroswser()

    import time
    time.sleep(10)