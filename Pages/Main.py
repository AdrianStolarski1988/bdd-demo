from Functions.Base import Base
from selenium.webdriver.common.by import By

search_bar = "s"
hints = '//div[@class="autocomplete-suggestions "]'
elements_founded = 'div[@class="autocomplete-products-all-link"]'
search_btn = '.search-widget__button'


class MainSite(Base):

    def search_product_by_name(self, words):
        search = self.driver.find_element(By.NAME, search_bar)
        search.clear()
        search.send_keys(words)

    def hint_is_displayed(self):
        self.check_element_is_displayed(By.XPATH, hints)

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, search_btn).click()


