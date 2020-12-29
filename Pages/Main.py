import time

from selenium.webdriver import ActionChains

from Functions.Base import Base
from selenium.webdriver.common.by import By

search_bar = "s"
hints = '//div[@class="autocomplete-suggestions "]'
elements_founded = 'div[@class="autocomplete-products-all-link"]'
amount_of_products = "//*[@class='autocomplete-product__last-text']"
search_btn = '.search-widget__button'
menu_main_categories = "//*[@id='top-menu']/li[number]"
subcategory = "/div/div/ul/li/a[element]"


menu_category = menu_main_categories.replace("number", "3")
menu_subcategory = "//*[contains(text(), 'category')]"

class MainSite(Base):

    def search_product_by_name(self, words):
        search = self.driver.find_element(By.NAME, search_bar)
        search.clear()
        search.send_keys(words)

    def hint_is_displayed(self):
        self.check_element_is_displayed(By.XPATH, hints)

    def amount_of_find_products_is_displayed(self):
        amount_find_products = self.driver.find_element(By.XPATH, amount_of_products).text
        return amount_find_products.split("(")[1][:-1]

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, search_btn).click()

    def hover_on_one_of_the_main_menu(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, menu_category))
        action.perform()

    def chose_subcategory(self, category_name):
        self.driver.find_element(By.XPATH, menu_subcategory.replace("category", category_name)).click()
