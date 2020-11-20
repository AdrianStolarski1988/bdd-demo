from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Main import Main

filter_select= "//span[@class='select2-selection select2-selection--single']"
search_input = ".select2-search__field"
thumbnail = "//*[@class='thumbnail']"



class Task2Page(Main):

    def count_amount_of_products(self):
        return len(self.driver.find_elements_by_xpath(thumbnail))


    def click_on_select_bar(self):
        self.driver.find_element_by_xpath(filter_select).click()


    def enter_category_to_search_bar(self, text):
        self.driver.find_element(By.CSS_SELECTOR, search_input).send_keys(text)


    def press_enter_button(self):
        self.driver.find_element(By.CSS_SELECTOR, search_input).send_keys(Keys.ENTER)


