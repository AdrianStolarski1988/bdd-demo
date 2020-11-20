import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL = "https://testingcup.pgs-soft.com/"


    def verify_exist_element(self, element):
        try:

            return WebDriverWait(self.driver, 4).until(ec.presence_of_element_located((By.XPATH, element)))
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshot("screenshots/not_find_expected_element.png")
            return False
        finally:
            pass


    def check_element_is_displayed(self, element):
        try:
            return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, element)))
        except NoSuchElementException as e:
            logging.error(e)
            logging.warning("not found element")
            return False
        # return True

    def go_to(self, website):
        self.driver.get(website)

def screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TimeoutException, NoSuchElementException) as e:
            args[0].driver.save_screenshot("screenshots/error.png")
            logging.error(e)
            return False
    return wrapper


