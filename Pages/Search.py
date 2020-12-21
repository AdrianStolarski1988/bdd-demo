from Functions.Base import Base
from selenium.webdriver.common.by import By

header_desc = "//*[@class='page-header page-header--search']/h1"
product_box = '//div[@class="card card-product"]'
elements_founded = 'div[@class="autocomplete-products-all-link"]'
search_btn = '.search-widget__button'


class SearchPage(Base):

    def search_word_is_displayed_in_search_header(self):
        return self.find_element(By.XPATH, header_desc).text

    def list_of_products(self):
        return len(self.driver.find_elements(By.XPATH, product_box))
