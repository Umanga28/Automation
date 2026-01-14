from Base.InitiateDriver import startBrowser, closeBroswser
from Library.ConfigReader import ElementsRead
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_InvalidateRegistration():
    driver = startBrowser()
    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'fname'))
    )).send_keys("Umanga")

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'lname'))
    )).send_keys("Yogi")

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'birth_month'))
    )).send_keys("September")

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'birth_date'))
    )).send_keys("13")

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'birth_year'))
    )).send_keys("2003")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, ElementsRead('Registration', 'a'))
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'email'))
    )).send_keys("9809569428")

    wait.until(EC.presence_of_element_located(
        (By.NAME, ElementsRead('Registration', 'password'))
    )).send_keys("Umanga@1234")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, ElementsRead('Registration', 'submit'))
    )).click()

    closeBroswser()
